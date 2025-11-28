def percentageLetter( s, letter):
    
    count = s.count(letter)

    res = int((count / float(len(s))) * 100)

    return res

s = "foobar"
letter = "o"
print(percentageLetter(s, letter))