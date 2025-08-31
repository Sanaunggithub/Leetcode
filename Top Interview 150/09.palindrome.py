def isPalindrom(x):
    # negative numbers and numbers ending with 0 can't be palindromes (except 0)
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    half = 0

    while half < x:
        half = half * 10 + x % 10
        x = x // 10
    
    # even case or odd case
    return x == half or x == half // 10


x = 121
print(isPalindrom(x))