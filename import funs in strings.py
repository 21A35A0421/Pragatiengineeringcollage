import re
str1="she sell sea shell in beach"
str2="sells"
if re.match(str2,str1):
    print('match found')
else:
    print('not found')


#similarly search
import re
str1="she sell sea shell in beach"
str2="sell"
if re.search(str2,str1):
    print('match found')
else:
    print('not found')



#finding ovels
import re
p=r"[aeiou]"
if re.search(p,"aeiou"):
    print("found")

