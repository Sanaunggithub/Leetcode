def reversePrefix(word, ch):

    if ch not in word:
        return word
    
    pos = word.find(ch)

    l = [w for w in word]

    res = l[:pos + 1] 

    res.reverse()
    res = res + l[pos + 1:]

    return "".join(res)

# return word[:pos+1][::-1] + word[pos+1:]


word = "xyxzxe"
ch = "z"

print(reversePrefix(word, ch))