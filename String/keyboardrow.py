def findWords(words):

    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    
    res = []

    for word in words: 
        left = 0
        while left < len(rows):
            for w in word.lower():
                if w not in rows[left]:
                    break
            
            # else works only when if not break
            else:
                res.append(word)

            left += 1

    return res

words = ["Hello","Alaska","Dad","Peace"]
print(findWords(words))

