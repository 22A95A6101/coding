a,b= map(int,input().split())
t = 2
lcm =1
while True:
    if a<t or b<t :
        break
    if a%t==0 and b%t ==0:
        a = a//t
        b = b//t
        lcm = lcm*t
    else:
        t+=1
print(lcm*a*b)
