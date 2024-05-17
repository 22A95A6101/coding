low,high=map(int,input().split())
for i in range(low,high+1):
    
    if i%5==0:
        continue
    print(i,end="")
