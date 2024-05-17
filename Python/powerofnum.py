base = int(input())
expo = int(input())
res=1
#for i in range(0,expo):
    #res*=base
    #i+=1
#print(res)
#while expo!=0:
    #res*=base
   # expo-=1
for i in range(expo,0,-1):
    res*=base
print(res)
