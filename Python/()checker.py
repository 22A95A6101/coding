class Solution:
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        stack = []

        for char in x:
            if char in ['(', '{', '[']:
                print(char)
                stack.append(char)
                print("stack",stack)
            else:
                # If the stack is empty, there is no corresponding opening bracket
                if not stack:
                    return False
                
                # Check if the current closing bracket matches the top of the stack
                top = stack.pop()
                print("top",top,)
                if (char == ')' and top == '(') or \
                   (char == '}' and top == '{') or \
                   (char == ']' and top == '['):
                    return True

        # If the stack is empty, all brackets are balanced
        return not stack

# Example usage:
sol = Solution()
exp1 = "{([])}"
exp2 = "()"
exp3 = "([]"
exp4 = "[({[([{}])]})}"

print(sol.ispar(exp1))  # Output: True
