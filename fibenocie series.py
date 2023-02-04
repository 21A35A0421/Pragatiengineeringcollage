#write a prodram to print the fibonoccie series using recurssion by funtions till 7 terms
def fib(n):
    if n<2:
        return 1
    return(fib(n-1)+fib(n-2))
n=int(input())
for i in range(n):
    print(fib(i),end=" ")
