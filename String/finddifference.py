def findTheDifference(s, t):
    s = sorted(s) # sort to ensure exact index comparison eg. 
    t = sorted(t) 

    left = 0
    while left < len(s):
        if s[left] != t[left]: # if characters differ, return the character from t
            return t[left]

        left += 1
    return t[left] # it must be the last character


s = ""
t = "y"

print(findTheDifference(s, t))