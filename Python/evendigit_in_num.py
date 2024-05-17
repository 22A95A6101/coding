def reverse_num(num):
    res=0
    c=1
    while num!=0:

        r = num%10
        num = num//10
        if r%2==0:
            res = r*c+res
            c=c*10
    return res
    
num= int(input())
res=reverse_num(num)
print(res)
