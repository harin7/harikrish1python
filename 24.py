h1=int(input())
h2=[int(x) for x in input().split()]
S=sorted(h2)
for y in range(h1):
    print(S[y],end=' ')
