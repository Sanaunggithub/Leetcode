def truncateSentence(s, k):
    l = s.split(" ")
    res = []

    for h in l:
        if k <= 0:
            break
        res.append(h)
        k -= 1

    return " ".join(res)


s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))