def is_prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True




def reverse(num):
    res=0
    while True:
       r = num%10
       num = num//2
       res = res*10+r
    return res

num = int(input())
res1 = is_prime(num)
if res1==True:
    print("prime")
    num1 = reverse(num)
    res1=is_prime(num1)
    if res1==True:
        print("Circular prime")
    else:
        print("not Circular")
else:
    print("not prime")
    
    
