N,A,D=map(int,input().split())
h=0
for j in range(0,N+1):
    h=h+(A+(j-1)*D)
print(h)
