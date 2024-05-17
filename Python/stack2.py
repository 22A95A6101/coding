from sys import maxsize
def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item+"pushed to stack")
def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize-1)
    return stack.pop()
def peek(stack):
    if(isEmpty(stack)):
        return str(-maxsize-1)
    return stack[len(stack)-1]
stack = createStack()
push(stack,str(50))
print(pop(stack)+"is popped")
