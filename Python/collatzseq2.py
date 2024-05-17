def col(n):
    oc =0
    ec=0
    num=0
    evensum=0
    oddsum=0
    largestnum=n
    while True:
        if n==1:
            oc+=1
            num+=n
            oddsum+=n
            break
        if n%2==0:
            ec+=1
            n=n//2
            num+=n
            evensum+=n
           
        else:
            oc+=1
            n=3*n+1
            num+=n
            oddsum+=n
    
    return ec,oc,num,evensum,oddsum,largestnum
      
            



n = int(input())
res = col(n)
print(res)
print("Even count:",res[0])
print("Od count:",res[1])
