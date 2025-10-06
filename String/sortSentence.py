def sortSentence(s):

    s = s.split()  
    res = [None] * len(s)

    for w in s:
        index = int(w[-1]) - 1
        res[index] = w[:-1] # insert is not safer.
        
    return " ".join(res)


s = "lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"
print(sortSentence(s))