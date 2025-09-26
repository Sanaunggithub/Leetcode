def scoreOfString(s):

    total = 0

    for i in range(len(s)):
        if i + 1 < len(s):
            total = total + abs(ord(s[i]) - ord(s[i + 1]))

    return total
s = "zaz"
print(scoreOfString(s))