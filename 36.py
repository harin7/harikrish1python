import re
h=raw_input()
new=re.sub('[\w+]','',h)
print(len(new))
