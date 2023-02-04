#geomatric series combination of different nums
#series:-1,1,2,3,4,9,8,27,16
term=int(input('enter num'))
if term%2==0:
    term=term//2
    print(3**(term-1))
else:
    term=term//2+1
    print(2**(term-1))
