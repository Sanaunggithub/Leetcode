def plusOne(digits):

    right = len(digits) - 1

    while right >= 0:
        if digits[right] < 9:
            digits[right] +=1
            return digits

        else:
            digits[right] = 0
            
        right -= 1

    digits.insert(0, 1)
    return digits

digits = [1,9,9,9]

print(plusOne(digits))