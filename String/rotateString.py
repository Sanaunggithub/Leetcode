def rotateString(s, goal):
    if len(s) != len(goal):
            return False

    count = 0

    for i in range(len(s)):
        if(s == goal):
            return True
    
        s = s[1:] + s[0]
        print(s)
        count += 1
    
   
    return False

s = "abcde"
goal = "abced"
print(rotateString(s, goal))