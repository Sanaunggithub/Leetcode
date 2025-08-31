# my solution
# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
        
#     return sorted(s) == sorted(t)

#  Time Complexity:
# O(n log n + m log m)

# Space Complexity:
# O(n + m)


# second solution
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    counts, countt = {}, {}

    for i in range(len(s)):
        # counts[s[i]] = 1 + counts[s[i]] this will throw error if key does not exist
        counts[s[i]] = 1 + counts.get(s[i], 0)
        countt[t[i]] = 1 + countt.get(t[i], 0)
    
    for c in counts:
        if counts[c] != countt.get(c, 0):
            return False
    return True

# time complexity : O(n+m)
# space complexity: O(n+m)

# third solution
#   return Counter(s)== Counter(t)

s = "jar"
t = "jam"
isAnagram(s, t)
