def isSubsequence(s, t):

    left = 0

    if len(s) == 0:
        return True
    
    for right in range(len(t)):
        if t[right] == s[left]:
            left += 1
    
        if left == len(s):
            return True

    return False

s = ""
t = "ahbgdc"

print(isSubsequence(s, t))