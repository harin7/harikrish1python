h=int(input())
i=[int(y) for y in input().split()]
r=sorted(i)
for x in range(h):
    print(r[x],end=' ')
