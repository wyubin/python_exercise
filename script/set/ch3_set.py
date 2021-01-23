#!/usr/bin/env python3
import os
import sys
import json
import copy
scriptDir = os.path.split(os.path.realpath(__file__))[0]

class pkg():
    """ch3_dict.py:
    execise python dict, 請存檔為 ans_ch3_dict.py
    """
    def __init__(self):
        self.args={}
        self.prepare()
        self.vars = {'ans':{}}
    
    def prepare(self):
        "認識 set 變數"
        self.args['roles']={"yubin":{'warlock','warrior'},"shaohua":{'demon_hunter','paladin','priest'}}
    
    def q1(self):
        "加入 'paladin' 到 yubin 用的角色, 提示 add"
        self.args['roles'] ## change
        return self.args['roles']['yubin']
    
    def q2(self):
        "將 'warlock','priest' 加到 shaohua 用的角色, 提示 update"
        self.args['roles'] ## change
        return self.args['roles']['shaohua']
    
    def q3(self):
        "依據使用角色數目由大到小排序使用者, 提示sort"
        ans = sorted(self.args['roles'].keys()) ## change
        return ans
    
    def q4(self):
        "將 'warrior'角色從 yubin 的使用角色中刪除, 提示 discard "
        self.args['roles'] ## change
        return self.args['roles']['yubin']

    def q5(self):
        "請列出 yubin 與 shaohua 兩人加起來使用的所有角色, 提示 union"
        ans = self.args['roles']['yubin'] ## change
        return ans

    def q6(self):
        "請列出 yubin 與 shaohua 都有使用的角色, 提示 intersection"
        ans = self.args['roles']['yubin'] ## change
        return ans
    
    def q7(self):
        "請列出 yubin 使用但 shaohua 不使用的角色, 提示 difference"
        ans = self.args['roles']['yubin'] ## change
        return ans

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
