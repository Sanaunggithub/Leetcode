def mergeAlternately(word1, word2):
        
    
    res = []

    l = max(len(word1), len(word2))
    for i in range(l):
        res.append(word1[i] if i < len(word1) else "")
        res.append(word2[i] if i < len(word2) else "")
    
    return "".join(res)


word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))