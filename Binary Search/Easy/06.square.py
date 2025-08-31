def mySqrt(x):
    # 0 ... x
    left, right = 0, x

    result = 0

    while left <= right:
        # mid-point formula to prevent overflow
        mid = left + ((right -left) // 2)

        if mid*mid > x:
            right = mid - 1 # discard right half

        elif mid*mid < x:
            left = mid + 1 # Discard left half
            result = mid   # Update result to the last valid mid
            
        else:
            return mid
    
    return result

print(mySqrt(8))