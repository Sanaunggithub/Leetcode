def minDistance(self, word1, word2):
    
    # cache array with additional row and col
    cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

    # bottom row (3, 2, 1, 0)
    for j in range(len(word2) + 1):
        cache[len(word1)][j] = len(word2) - j
    # last col (3, 2, 1, 0)
    for i in range(len(word1) + 1):
        cache[i][len(word2)] = len(word1) - i

    # start from bottom to up
    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                cache[i][j] = cache[i + 1][j + 1]
            else:
                cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])

    return cache[0][0] # total min distance will store in this position