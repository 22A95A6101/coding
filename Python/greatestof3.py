a = int(input())
b = int(input())
c = int(input())
#result = max(a,max(b,c))
#print(result,"is greater")
temp = a if a>b else b
result = temp if temp>c else c
print(str(result)+"is greater")
