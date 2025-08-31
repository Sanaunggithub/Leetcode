def uncommonFromSentences(s1, s2):
    word_count = {}
    lst1 = s1.split()
    lst2 = s2.split()
    res = []

    # count each word
    for word in lst1 + lst2:
        word_count[word] = word_count.get(word, 0) + 1

    for word in word_count:
        if word_count[word] == 1:
            res.append(word)
    print(word_count)

    return res
        
s1 = "apple apple"
s2 = "banana"

print(uncommonFromSentences(s1, s2))