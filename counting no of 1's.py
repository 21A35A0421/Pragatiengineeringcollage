n=int(input("enter no .of terms"))
x=input('enter data')
l=list(x)
sum=0
for j in l:
    if l[0]==1:
        pass
    elif j=='1':
        sum+=1
print(sum-1)
