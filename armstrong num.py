su=0
n=(int(input('enter num')))
while(n!=0):
    r=n%10
    su+=r**3
    n=n//10
if(sum==n):
    print('armstrong number')
else:
    print('not a armstrong num')
