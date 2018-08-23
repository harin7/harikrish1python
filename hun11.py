h=[x for x in input().split()]
c=[]
for i in range(0,len(h)):
    f=''
    ch=h[i]
    for j in range(0,len(ch)):
        f=ch[j]+f
    if i<len(h)-1:
        k=' '
    else:k=''
    print(f,end=k)
