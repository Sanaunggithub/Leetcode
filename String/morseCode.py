def uniqueMorseRepresentations(words):

    cToM = {
            'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',  'e': '.',     'f': '..-.',
            'g': '--.',   'h': '....',  'i': '..',    'j': '.---', 'k': '-.-',   'l': '.-..',
            'm': '--',    'n': '-.',    'o': '---',   'p': '.--.', 'q': '--.-',  'r': '.-.',
            's': '...',   't': '-',     'u': '..-',   'v': '...-', 'w': '.--',   'x': '-..-',
            'y': '-.--',  'z': '--..'
        }
    
    res = set()

    for word in words:
        s = ""
        for c in word:
            s += cToM[c]

        res.add(s)
    
    return len(res)
    

words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))


