def maxFreqSum(s):
    vowel = {}
    consonant = {}

    for c in s:
        if c in 'aeiou':
            vowel[c] = vowel.get(c, 0) + 1
        
        else:
            consonant[c] = consonant.get(c, 0) +1

    sum = 0
    max_v = 0 if not vowel else  max(vowel.values())
    max_c = 0 if not consonant else max(consonant.values())

    return max_v + max_c


s = "aeiaeia"
print(maxFreqSum(s))