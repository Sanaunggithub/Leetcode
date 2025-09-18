def addBinary(a, b):
    res = ""
    carry = 0

    # start adding from the right digit
    a, b = a[::-1], b[::-1]

    # loop through the max length of the string
    for i in range(max(len(a), len(b))):
        # The ord(...) - ord("0") trick is just a way to turn a digit character into an integer.
        digitA = ord(a[i]) - ord("0") if i < len(a) else 0
        digitB = ord(b[i]) - ord("0") if i < len(b) else 0

        total = digitA + digitB + carry
        char  = str(total % 2)
        res   = char + res
        carry = total  // 2
    
    # three-digit case

    if carry:
        res = "1" + res
    
    return res

a = "11"
b = "1"
print(addBinary(a, b))

# ord("7") - ord("0") = 55 - 48 = 7
# ord("3") - ord("0") = 51 - 48 = 3

# a = "11", b = "1"

# Reverse them:

# a = "11"

# b = "1"

# First loop (i=0):

# digitA = 1, digitB = 1

# total = 1 + 1 + 0 = 2

# char = str(2 % 2) = str(0) = "0"

# res = "0" + "" = "0"

# carry = 2 // 2 = 1

# Second loop (i=1):

# digitA = 1, digitB = 0 (since b is shorter)

# total = 1 + 0 + 1 = 2

# char = str(2 % 2) = "0"

# res = "0" + "0" = "00"

# carry = 2 // 2 = 1

# Loop ends, but carry = 1:

# res = "1" + "00" = "100"

    