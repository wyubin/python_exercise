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
        #self.args = json.load(open(os.path.join(scriptDir, 'ch3_dict.json')))
        self.prepare()
        self.vars = {'ans':{}}
    
    def prepare(self):
        "認識 dict 字典變數"
        self.args['roles']={"yubin":['warlock','warrior'],"shaohua":['demon_hunter','paladin','priest']}
    
    def q1(self):
        "指定出 yubin 喜歡用的角色"
        ans = self.args['roles']["yubin"] ## change
        return ans
    
    def q2(self):
        "列出有哪些人在角色使用列表中, 提示: keys"
        ans = self.args['roles'].keys() ## change
        return ans
    
    def q3(self):
        "列出共有哪些角色, 提示: values"
        ans = set()
        ans.update(self.args['roles']["yubin"]) ## change
        ans.update(self.args['roles']["shaohua"]) ## change
        return ans
    
    def q4(self):
        "依據使用角色數量由大到小列出名字, 提示: sort"
        ans = sorted(self.args['roles'].keys(), key =lambda x:len(self.args['roles'][x]), reverse=False ) ## change
        return ans

    def q5(self):
        "請幫 yubin 加入 paladin 作為喜歡使用的角色之一, 提示 append"
        self.args['roles']["yubin"].append('paladin')## change
        ans = set(self.args['roles']['yubin'])
        return ans

    def q6(self):
        "請加入 fanglin, 並加入她喜歡的角色 druid 還有 hunter, 提示 update"
        self.args['roles'].update({'fanglin':["druid",'hunter']}) ## change
        return self.args['roles'].get('fanglin')

    def main(self):
        indQ=1
        currQ=getattr(self,f'q{indQ}',False)
        while currQ:
            ans = currQ()
            print(currQ.__doc__)
            print(f'答案{indQ}:{ans}')
            self.vars['ans'][f'q{indQ}'] = ans
            indQ += 1
            currQ = getattr(self,f'q{indQ}',False)

if __name__ == '__main__':
    a=pkg()
    a.main()
