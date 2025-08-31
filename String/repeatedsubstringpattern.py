def repeatedSubstringPattern(s):
    n = len(s) 

    
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            substring = s[:i]

        if substring * (n // i) == s:
            return True

    return False


# Iteration 1:
#   size = 1
#   block = 'a'
#   repeats = 12
#   built = 'aaaaaaaaaaaa'
#   matches = False

# Iteration 2:
#   size = 2
#   block = 'ab'
#   repeats = 6
#   built = 'abababababab'
#   matches = False

# Iteration 3:
#   size = 3
#   block = 'abc'
#   repeats = 4
#   built = 'abcabcabcabc'
#   matches = True

# Final result: True


