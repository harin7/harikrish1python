h1=int(input())
h2=[int(y) for y in input().split()]
for x in range(h1):
    print(h2[x],x,sep=' ',end="\n")
