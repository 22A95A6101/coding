low,high=map(int,input().split())
#while low<=high:
for i in range(low,high+1):
    print(i, end="")
    if i%13==0:
        break
    
