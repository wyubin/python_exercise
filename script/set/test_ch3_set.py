import os
import sys
import json
import copy
import unittest
scriptDir = os.path.split(os.path.realpath(__file__))[0]
from ans_ch3_set import pkg as funcMain 

class testFunc(unittest.TestCase):
    def setUp(self):
        #self.q2ans = json.load(open(os.path.join(scriptDir, 'ans_ch3_dict.json')))
        self.instMain = funcMain()
        self.q2ans = self.getAns()

    def getAns(self):
        roles = copy.deepcopy(self.instMain.args['roles'])
        roles['yubin'].add('paladin')
        q2ans = {'q1':copy.copy(roles['yubin'])}
        
        roles['shaohua'].update({'warlock','priest'})
        q2ans['q2'] = copy.copy(roles['shaohua'])
        
        q2ans['q3'] = sorted(roles.keys(), key= lambda x:len(roles[x]), reverse=True)

        roles['yubin'].discard('warrior')
        q2ans['q4'] = copy.copy(roles['yubin'])

        q2ans['q5'] = roles['yubin'].union(roles['shaohua'])

        q2ans['q6'] = roles['yubin'].intersection(roles['shaohua'])

        q2ans['q7'] = roles['yubin'].difference(roles['shaohua'])

        return q2ans

    def test_ans(self):
        self.instMain.main()
        for tkey,tval in sorted(self.instMain.vars['ans'].items(),key=lambda x:int(x[0][1:])):
            with self.subTest(tkey=tkey,tval=tval):
                self.assertEqual(tval, self.q2ans[tkey])

if __name__ == '__main__':
    unittest.main()
