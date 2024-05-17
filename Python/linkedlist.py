class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
a=[10,20,30,40,50]
head=Node(a[0])
h=head
for i in  range(1,len(a)):
    h.next=Node(a[i])
    h=h.next
while head:
    print(head.data)
    head=head.next









#head=Node(10)
#h=head
#h.next=Node(20)
#h=h.next
#print(h.data)
#h.next=Node(30)
#h=h.next
#print(h.data)

#h.next=Node(40)
##print(h.data)






