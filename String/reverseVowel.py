def reverseVowels(s):
    vowel ='aeiouAEIOU'
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] not in vowel:
            left += 1

        elif s[right] not in vowel:
            right -= 1
        
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
    return "".join(s)
        
        
s = "A man, a plan, a canal: Panama"

print(reverseVowels(s))