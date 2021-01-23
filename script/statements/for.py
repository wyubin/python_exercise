#!/usr/bin/env python3
import os
import sys
import copy
scriptDir = os.path.split(os.path.realpath(__file__))[0]

class pkg():
    """for.py:
    execise python dict, 請存檔為 ans_for.py
    """
    def __init__(self):
        self.args={}
        self.prepare()
        print(self.prepare.__doc__)
        self.vars = {'ans':{}}
    
    def prepare(self):
        "以 for loop 處理資料，scores 是班上同學的分數(list), total_score 是紹華的每一科分數(dict)"
        self.args['scores']=[50,40,55,38]
        self.args['total_score']={'國語':90,'社會':86,'數學':97,'自然':92}
    
    def q1(self):
        "老師說大家都考得很爛，乾脆都乘以2來當作最後分數"
        score_new=[]
        for score in []: ## change
            score_new.append('') ## change
        return score_new
    
    def q2(self):
        "要做紹華的成績單，輸出列表，把科目跟分數中間加'=' "
        strScore=[]
        for substract,score in self.args['total_score'].items():
            strScore.append(''.format(substract,score)) ## change
        return set(strScore)
    
    def q3(self):
        "老師發現有人超過100分，所以當分數調整兩倍時超過100的話，就當作是100"
        score_new=[]
        for score in []: ## change
            score = score*2
            if score==1: ## change
                score = 100
            score_new.append(score)
        return score_new

    def main(self):
        indQ=1
        currQ=getattr(self,f'q{indQ}',False)
        while currQ:
            ans = currQ()
            print(currQ.__doc__)
            print(f'答案{indQ}:{ans}')
            self.vars['ans'][f'q{indQ}'] = copy.copy(ans)
            indQ += 1
            currQ = getattr(self,f'q{indQ}',False)

if __name__ == '__main__':
    a=pkg()
    a.main()
