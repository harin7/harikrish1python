s1,s2=map(str,input().split())
h1=len(s1)
h2=len(s2)
count=0
if(h1==h2):
    for i in range(h1):
        if(s1[i]==s2[i]):
            count=count+0
        else:
            count=count+1
if(count==1):
        print("yes")
else:
        print("no")
