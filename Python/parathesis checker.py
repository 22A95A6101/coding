def bracketsbalanced(expr):
    stack=[]
    for char in expr:
        if char in ["(","[","{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            top=stack.pop()
            if top=='(':
                if char!=")":
                    return False
            if top=='{':
                if char!="}":
                    return False
            if top=='[':
                if char!="]":
                    return False
    if stack:
        return False
    return True
                
                

    




expr="{(}[]"
if bracketsbalanced(expr):
    print("balanced")
else:
    print("not balanced")
