def romanToInt(s):
    rtoi = {"I" : 1, "V" : 5, "X" :10, "L": 50,
            "C" : 100, "D": 500, "M": 1000
            }
    
    num = 0

    for i in range(len(s)):
        if i + 1 < (len(s)) and rtoi[s[i]] < rtoi[s[i+1]]:
            num -= rtoi[s[i]]
        
        else:
            num += rtoi[s[i]]

    return num

s = "MCMXCIV"
print(romanToInt(s))
