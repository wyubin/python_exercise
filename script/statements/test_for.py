import os
import sys
import json
import copy
import unittest
scriptDir = os.path.split(os.path.realpath(__file__))[0]
from ans_for import pkg as funcMain 

class testFunc(unittest.TestCase):
    def setUp(self):
        self.instMain = funcMain()
        self.q2ans = self.getAns()

    def getAns(self):
        q2ans = {'q1':[x*2 for x in self.instMain.args['scores']]}

        q2ans['q2'] = set(['{}={}'.format(x,y) for x,y in self.instMain.args['total_score'].items()])
        
        q2ans['q3'] = [x*2 if x*2 <= 100 else 100 for x in self.instMain.args['scores']]

        return q2ans

    def test_ans(self):
        self.instMain.main()
        for tkey,tval in sorted(self.instMain.vars['ans'].items(),key=lambda x:int(x[0][1:])):
            with self.subTest(tkey=tkey,tval=tval):
                self.assertEqual(tval, self.q2ans[tkey])

if __name__ == '__main__':
    unittest.main()
