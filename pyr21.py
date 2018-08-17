h1,i1=map(int,input().split())
h2,i2=map(int,input().split())
h3,i3=map(int,input().split())
if((h1*(i2-i3)+h2*(i3-i1)+h3*(i1-i2))==0):
    print ("yes")
else:
    print ("no")
