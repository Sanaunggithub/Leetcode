def checkIfPangram(sentence):
    count = {}

    for c in sentence.lower():
        if c.isalpha():
            count[c] = count.get(c, 0) + 1
  
    return len(count) == 26 # count the number of unique letters (key)

sentence = 'leetcode'
print(checkIfPangram(sentence))