number = int(raw_input())
count=0

if number > 1:
    for i in range(1, number+1):
        if ((number % i) == 0):
        	count+=1
    if(count==2):
    	print("yes")
            
    else:
    	print("no")
