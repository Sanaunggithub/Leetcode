def isValid(s):
    p = {')': '(', ']': '[', '}': '{'}
    
    # If the stack is empty → all brackets matched → return True.
    # If there’s anything left in the stack → unmatched opening brackets → return False.
    stack = []
    for i in range(len(s)):
        if s[i] in "[({":
            stack.append(s[i])

        else:
            if not stack or p[s[i]] != stack.pop(): # not stack checks if the stack is empty because we cannot pop from an empty stack
                return False
    
    return not stack