def repeatedCharacter(s):
    seen_letters = []

    for c in s:
        if c not in seen_letters:
            seen_letters.append(c)
        
        else:
            return c


s = "abccbaacz"
print(repeatedCharacter(s))