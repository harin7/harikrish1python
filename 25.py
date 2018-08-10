h1=int(input())
h2=[int(b) for b in input().split()]
s=sorted(h2)
if h1%2==0:
    a=((h1)-1)//2
    b=x+1
    c=(s[a]+s[b])/2
    print(c)
else:
    a=(h1)//2
    print(s[a])
