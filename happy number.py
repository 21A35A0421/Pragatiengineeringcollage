#happy number
n=int(input('enter number'))
b=[]
b.append(n)
s=0
x=b[-1]
while x!=1:
    a=b[-1]
    while a!=0:
        r=a%10
        a=a//10
        s=s+(r*r)
    b.append(s)
    x=b[-1]
    s=0
print(b)
if b[-1]!=1:
    print('not happy number')
else:
    print('happy number')
