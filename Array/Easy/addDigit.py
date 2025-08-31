def addDigits(num):
    if num <= 9: return num

    while num >= 10:
        s = 0
        for digit in str(num):
            s += int(digit)

        num = s
    
    return num