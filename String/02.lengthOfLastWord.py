def lengthOfLastWord(s):
    words = s.strip().split(" ")
    return len(words[len(words) - 1])

s = s = "   fly me   to   the moon  "

print(lengthOfLastWord(s))
     

     