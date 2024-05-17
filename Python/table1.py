num,x,y=map(int,input().split())
if x>y:
    for i in range(y,x+1):
        print(num,"X",i,"=",num*i)
else:
    for i in range(x,y+1):
        print(num,"X",i,"=",num*i)
