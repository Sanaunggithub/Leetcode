def reverseWords(s):

    s = s.split()
    res = []
    for c in s:
        res.append(c[::-1])
    
    return " ".join(res)

s = "Let's take LeetCode contest"
print(reverseWords(s))