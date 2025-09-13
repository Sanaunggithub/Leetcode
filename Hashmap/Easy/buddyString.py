def buddyStrings(s, goal):
    # If lengths are different, can't be buddy strings
    if len(s) != len(goal): return False

    if s == goal:
        return len(set(s)) < len(s)
    
    diffs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diffs.append(i)

    return len(diffs) == 2 and s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]

    
    

s = "ab"
goal = "ab"

print(buddyStrings(s, goal))


# s = "aa"
# goal = "aa"
# len(set(s)) = 1
# len(s) = 2
# 1 < 2 → True  (so "aa" has duplicates)

# s = "ab"
# goal = "ab"
# len(set(s)) = 2
# len(s) = 2
# 2 < 2 → False (no duplicates)

# s = "abcabc"
# goal = "abcabc"

# set(s) → {'a','b','c'}
# len(set(s)) = 3
# len(s) = 6
# Compare: 3 < 6 → ✅ True


# s = "ab"
# goal = "ba"

# diffs = [0,1]
# Check:
# s[0] == goal[1]  # 'a' == 'a' → True
# s[1] == goal[0]  # 'b' == 'b' → True
# Both True → swapping indices 0 and 1 fixes the string


# s = "abcd"
# goal = "badc"

# diffs = [0,1,2,3]  # 4 differences
# # Check only works if len(diffs) == 2
