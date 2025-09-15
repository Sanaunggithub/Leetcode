def canBeTypedWords(text, brokenLetters):
    text = text.split(" ")
    broken = set(brokenLetters)
    count = len(text)
  
    for word in text:
        word = set(word)
        if(broken & word):  # {'a','d'} ∩ {'w','o','r','l','d'} = {'d'}
            count -= 1
        
    return count

text = "hello world"
brokenLetters = "ad"
print(canBeTypedWords(text, brokenLetters))