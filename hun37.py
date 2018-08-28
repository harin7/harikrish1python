h=input()
temp=h
for i in range(97,123):
    h=h.replace(chr(i),'')
    if(h==h[::-1]):
        print('YES')
        break
    h=temp
    if(i==122):
        print('NO')
