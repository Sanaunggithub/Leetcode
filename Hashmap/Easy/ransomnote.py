def canConstruct(ransomNote, magazine):

    countr = {}
    countm = {}

    for i in range(len(ransomNote)):
        countr[ransomNote[i]] = countr.get(ransomNote[i], 0) + 1
    
    for i in range(len(magazine)):
        countm[magazine[i]] = countm.get(magazine[i], 0) + 1

    for c in countr:
        if countm.get(c, 0) < countr[c]:
            return False
    
    return True

ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))