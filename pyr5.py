h={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
j=[str(x)for x in input()]
sum=0
for i in range(0,len(j)):
    if i>0 and h[j[i]] > h[j[i-1]]:
        sum=h[j[i]]-h[j[i-1]]
    else:
        sum+=h[j[i]]
print(sum)
