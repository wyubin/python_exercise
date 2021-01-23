import math
## 使用nameTmp存字串"hello,yubin!!" 到 ans 變數
nameTmp='yubin'
ans='hello,'+nameTmp
print('答案1：'+ans)

## 將ans 變成 ["hello,'yubin' !!"], 需要包含'跟"
ans=f'\"hello,\'{nameTmp}\' !!\"'
print('答案2：'+ans)

## 使用字串功能將數字塞進 ans, 提示：format
money=100
money_apple=12
get_apple=money/money_apple
ans=f'我有{money}元, 蘋果一顆{money_apple}元, 可以買{get_apple:.0f}顆蘋果'
print('答案3：'+ans)

## 將身高紀錄(strList)轉成身高列表(listHeight), 提示 split
strList='133,141,124,135'
listHeight=strList.split(',')
print('答案4：{}'.format(listHeight))

## 將身高列表(listHeight)轉回身高紀錄, 提示join
ans=','.join(listHeight)
print('答案5：{}'.format(ans))

##承上，直接列出第三人身高
ans=listHeight[2]
print('答案6：'+ans)

##承上，將 listHeight 由低至高排序後列出, 提示: sort
ans=list(map(int,listHeight))
ans.sort()
print('答案7：{}'.format(ans))

## 老師發現第三個人記錯了, 是 126, 請修改
listHeight[2]=126
print('答案8：{}'.format(listHeight))

## 要刪除地一個人的身高紀錄
#del listHeight[0]
listHeight.pop(0)
print('答案9：{}'.format(listHeight))

##承上，將 listHeight 由高至低排序後列出, 提示: sort
ans=list(map(int,listHeight))
ans.sort(reverse=True)
print('答案10：{}'.format(ans))
