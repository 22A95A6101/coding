n=int(input())
if n==0 or n==1:
    print("notprime")
if ((n*n-1)%24)==0:
    print("prime")
else:
    print("not a prime")
