def countConsistentStrings( allowed, words):
    count = 0
    for word in words:
        for ch in word:
            if ch not in allowed:
                break
        else:
            count += 1
    return count
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

print(countConsistentStrings(allowed, words))