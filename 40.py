n= int(input())
h1=1
h2=1
count=0
while count<n:
    print(h1,end=(' '))
    nth=h1+h2
    h1=h2
    h2=nth
    count+=1
