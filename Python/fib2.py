"""
fib
10
counter based loop
default
a=0
b=1
a+b

"""
def fib_seq(num,sh):
    a,b=0,1
    print(a,b,end=" ")
    for i in range(3,num+1,1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        if c == sh:
            print("yes")
num,sh=map(int,input().split())
fib_seq(num,sh)
