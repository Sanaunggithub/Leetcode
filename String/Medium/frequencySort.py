def frequencySort(s):
        
    c = {}
    for ch in s:
        c[ch] = c.get(ch, 0) + 1

    res = ""
    for k, v in sorted(c.items(), key=lambda x: (-x[1], x[0])):
        res += k * v

    return res

    

s = "Aabb"
print(frequencySort(s))