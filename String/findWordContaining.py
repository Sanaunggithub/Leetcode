class Solution(object):
    def findWordsContaining(words, x):
        index = []
        for i in range(len(words)):
            if x in words[i]:
                index.append(i)

        return index