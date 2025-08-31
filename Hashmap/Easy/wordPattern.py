def wordPattern(pattern, s):
    
    words = list(s.split())

    if len(words) != len(pattern):
        return False
    
    charToWord = {}
    wordToChar = {}
    
    for c, w in zip(pattern, words):
        if c in charToWord and charToWord[c] != w:
            return False
        
        if w in wordToChar and wordToChar[w] != c:
            return False
        
        charToWord[c] = w
        wordToChar[w] = c
        
    return True
    
    

pattern = "abba"
s =  "dog dog dog dog"

print(wordPattern(pattern, s))