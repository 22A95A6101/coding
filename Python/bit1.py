def decimal(a):
    d=0
    while(a):
        if(a&1)>0:
            d+=1
        a>>=1
    return d
def findcount(a,b):
    count=0
    for i in range(a,b+1):
       count+= decimal(i)
        
       
    return count
a=int(input())
b=int(input())

print(findcount(a,b))

