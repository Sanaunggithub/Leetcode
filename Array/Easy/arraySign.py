def arraySign(nums):       
    product = 1

    for n in nums:
        if n == 0:
            return 0
        product *= n


    if product > 0:
        return 1

    elif product < 0:
        return -1