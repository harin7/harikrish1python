a=int(input())
b=[int(y) for y in input().split()]
for x in range(a):
    print(b[x],x,sep=' ',end="\n")
