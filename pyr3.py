h1=int(input())
rev=0
while(h1>0):
    dig=h1%10
    rev=rev*10+dig
    h1=h1//10
print(rev)
