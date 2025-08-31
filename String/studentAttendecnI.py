def checkRecord(s):
    countA, countL = 0, 0

    for c in s:   
        if c == 'A':
            countA += 1
            countL = 0 # streak lose

        elif c == 'L':
            countL += 1
        
        else:
            countL = 0
        
        if countA >= 2 or countL >= 3:
            return False
    
    return True
s = "PPALLPL"
print(checkRecord(s))