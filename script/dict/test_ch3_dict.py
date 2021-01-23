import os
import sys
import json
import copy
import unittest
scriptDir = os.path.split(os.path.realpath(__file__))[0]
from ans_ch3_dict import pkg as funcMain 

class testFunc(unittest.TestCase):
    def setUp(self):
        #self.q2ans = json.load(open(os.path.join(scriptDir, 'ans_ch3_dict.json')))
        self.instMain = funcMain()
        self.q2ans = self.getAns()

    def getAns(self):
        roles = copy.copy(self.instMain.args['roles'])
        q2ans={
            'q1':roles['yubin'],
            'q2':roles.keys(),
            'q3':set(roles['yubin'] + roles['shaohua']),
            'q4':sorted(roles.keys(),key= lambda x:len(roles[x])),
        }
        roles['yubin'].append('paladin')
        roles['fanglin'] = ['druid','hunter']
        q2ans.update({
            'q5':set(roles['yubin']),
            'q6':roles.get('fanglin'),
        })
        return q2ans

    def test_ans(self):
        self.instMain.main()
        for tkey,tval in sorted(self.instMain.vars['ans'].items(),key=lambda x:int(x[0][1:])):
            with self.subTest(tkey=tkey,tval=tval):
                self.assertEqual(tval, self.q2ans[tkey])

if __name__ == '__main__':
    unittest.main()
