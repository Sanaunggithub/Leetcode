from collections import Counter

def commonChars(words):
    count = Counter(words[0]) # this will return a map of characters with their counts
    
    for w in words:
        current_word = Counter(w)
        
        for c in count:
            count[c] = min(count[c], current_word[c]) # take minimum count of each character to find common characters

    res = []

    for c in count:
        for i in range(count[c]):
            res.append(c)

    return res


words = ["bella","label","roller"]
print(commonChars(words))


# def commonChars(words):
#     common = Counter(words[0])
#     for word in words[1:]:
#         common &= Counter(word)  # keep only the min count of common characters
    
#     return list(common.elements())  # turn it into a list with duplicates