password = 'a123456'
x = 3
while x > 0:
    x = x-1
    pwd = input('請打出密碼: ')
    if pwd == password:
        print ('登入成功! ') 
        break
    else:
        if x > 0:
        print ('密碼錯誤! ', '還有', x,'次機會!' )
        else:
            print ('失敗三次，封鎖帳號')