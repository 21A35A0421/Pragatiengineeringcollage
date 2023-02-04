#0,0,7,6,14,12,21,18
term=int(input('enter term'))
if term%2==0:
    term=term//2
    print(6*(term-1))
else:
    term=term//2
    print(7*(term-1))
