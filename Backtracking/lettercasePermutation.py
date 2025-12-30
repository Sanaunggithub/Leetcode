def letterCasePermutation(s):
        
    res = []
    cur = []

    def dfs(i):
        if i >= len(s):
            res.append("".join(cur))
            return
        
        
        if s[i].isalpha():
            # lowercase branch
            cur.append(s[i].lower())
            dfs(i + 1)
            cur.pop()

            # uppercase branch
            cur.append(s[i].upper())
            dfs(i + 1)
            cur.pop()

        else:
            cur.append(s[i])
            dfs(i + 1)
            cur.pop()


    dfs(0)

    return res

s = "a1b2"
print(letterCasePermutation(s))