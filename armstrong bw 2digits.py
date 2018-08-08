h,i=input().split()
h=int(h)
i=int(i)
for x in range(h,i):
	temp=x
	num=0
	while x!=0:
		y=x%10
		x=x//10
		num += y**3
	if num==temp:
		print(temp,end=" ")
