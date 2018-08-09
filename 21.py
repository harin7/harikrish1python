
n,a,d=map(int,input().split())
h=0
for i in range(0,n+1):
    h=h+(a+(i-1)*d)
print(h)
