for a in range(20):#(0,10,1)--> i=0;i<10;i+=1
    print("Priya")
for i in range(10):
    print(i)
for j in range(1,10):
    print(j)
for k in range(1,10,2):
    print(k)
for l in range(1,10,5):
    print(l)
for m in range(200,100,-4):#backword looping 3 values should be mentioned
    print(m)
num = int(input())# if num =10 its prints 1to9 we have to print 10 also 
for s in range(num+1):#if we give 10 its takes 10+1=11 so its print 10 also
    print(s,end = "  ")#end prints  side by side
 
for r in range(num,0,-1):#backward loop
    print(r, end =" ")
