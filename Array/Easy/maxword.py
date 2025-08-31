def mostWordsFound(sentences):
    max = 0

    for word in sentences:
        word = word.split()
        if (len(word)) > max:
            max = len(word)
            
    print(max)


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
mostWordsFound(sentences)