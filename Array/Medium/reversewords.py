def reverseWords(s):

    words = s.split()

    right = len(words) - 1
    left = 0
    
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -=1

    return " ".join(words)


s = "the sky is blue"

print(reverseWords(s))