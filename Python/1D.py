num = int(input("Enter the Size of Array :"))
arr = []

print("The elements are : ")
for i in range(num):
    arr.append(int(input()))

print("The elements are : ")

for i in range(num):
    print(arr[i], end=" ")
