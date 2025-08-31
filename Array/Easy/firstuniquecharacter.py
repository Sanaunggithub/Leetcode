def firstUniqChar(s):
    
    count = {}

    for c in s:
        if c in count:
            count[c] += 1
        
        else:
            count[c] = 1

    for i,v in enumerate(count):
        if count[v] == 1:
            return i
        
    return -1
    

s = "loveleetcode"

print(firstUniqChar(s))


    