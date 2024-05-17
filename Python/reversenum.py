def reverse_num(num):
    res=0
    c=0
    while num!=0:
        c+=1
        r = num%10
        num = num//10
        
        res = res*10+r
    return res,c
    
num= int(input())
res=reverse_num(num)
print(res)
