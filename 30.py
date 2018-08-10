h,i=map(int,input().split())
j,k=map(int,input().split())
h0=(h*60)+i
t0=(j*60)+k
t1=h0-t0
h1=t1//60
t1%=60
print(h1,t1,sep=" ")
