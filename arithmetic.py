N,A,D=map(int,input().split())
num=0
for j in range(0,N+1):
    num=num+(A+(j-1)*D)
print(num)
