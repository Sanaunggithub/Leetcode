def finalString(s):
    res = []
    s = list(s)

    for c in s:
        if c == 'i':
            res.reverse()

        else:
            res.append(c)

    return "".join(res)

s = "string"
print(finalString(s))