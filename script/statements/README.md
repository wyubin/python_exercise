# statements

練習 for, if, while, try, with 等判斷句的使用方式

## for 迴圈
通常使用在需要依序處理一連串資料的情境, 那一連串資料通常為 list 單元, 或是 dict 的 key, 或是具有 .next interface 的物件(像是 file object)
```python
money = [5,7,9,12]
moneyX2 = []
## 依序把 money 中的每一個數字拿出來當作變數nt
for nt in money:
    moneyX2.append(nt*2)

## 如果 list 裡面每個有多個數字也可以同時拆開
money2 = [[40,50],[32,34],[53,45]]
for m1,m2 in money2:
    print('m1:{},m2:{}'.format(m1,m2))

## dict 直接使用則是拿出 key
money3 = {'yubin':50,'shaohua':45}
for user in money3:
    print('user:{},money:{}'.format(user,money3[user]))

## dict 可以用.items 變成key,value 並列的變數
money3 = {'yubin':50,'shaohua':45}
for user,mm in money3.items():
    print('user:{},money:{}'.format(user,mm))

## if 可以放在迴圈內去判斷狀況，決定是否要做不同處理
money3 = {'yubin':50,'shaohua':45}
for user,mm in money3.items():
    if user=='yubin':
        mm=mm*2
    print('user:{},money:{}'.format(user,mm))

```
