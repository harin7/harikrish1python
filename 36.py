import re
h1=raw_input()
new=re.sub('[\w+]','',h1)
print(len(new))
