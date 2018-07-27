#program to check whether the given letter is vowel or consonant#
xx=raw_input()
if((xx>='a' and xx<='z') or (xx>='A' and xx<='Z')):
	if(xx in ['a','e','i','o','u','A','E','I','O','U']):
		print('vowel')
	else:
		print('consonant')
else:
	print('invalid')
	
