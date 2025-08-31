def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res

        res += strs[0][i]  

    return s

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))


# strs = ["flow", "fl"]
# strs[0] = "flow"
# Loop: i = 0, 1 → OK
# i = 2:
# "fl" has length 2 → i == len("fl") → TRUE


# strs = ["fl", "flower", "flight"]
# strs[0] has length 2, so strs[0][2] → ❌ IndexError if accessed!
# But we don't get there, because the loop ends:
