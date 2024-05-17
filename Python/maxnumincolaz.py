def max_collatz_seq(num):
    big=num
    while True:
        if num>big:
            big=num
            
       
        if num==1:
             return big
        
        if num%2==0:
            num=num//2
        else:
            num=num*3+1
   
            
        



num=int(input())
res=max_collatz_seq(num)
print(res)
