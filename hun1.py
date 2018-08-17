h=raw_input()
i=0
j=0
new=[]
list=[int(x) for x in raw_input().split()]
while(i==0):
    l=list[i]
    list.remove(list[0])
    if((l in list)and(l not in new)):
        print l,
        new.insert(j,l)
        j+=1
    elif((new==[])and(list==[])):
        print('unique')
    if(list==[]):
        break
