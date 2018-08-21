h=int(input())
print("0" if h>0 and (h & (h-1))==0 else "1")
