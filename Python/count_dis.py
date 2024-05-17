arr=[30,50,10,20,40,10,20]
n=len(arr)
visited=[False]*n
count_dis=0
for i in range(n):
    if not visited[i]:
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                visited[j]=True
                count_dis+=1
print(count_dis)
