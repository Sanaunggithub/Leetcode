def halvesAreAlike(s):        
    count1 = 0
    count2 = 0
    
    l = len(s) // 2

    vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    for i in range(0, l):
        if s[i] in vowel:
            count1 += 1
        
    for i in range(l, len(s)):
        if s[i] in vowel:
            count2 += 1

    return count1 == count2