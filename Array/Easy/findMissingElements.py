def findMissingElements(nums):
        
    left = min(nums)
    right = max(nums)

    num_set = set(nums)
    res = []

    while left <= right:
        if left not in num_set:
            res.append(left)
        
        left += 1

    return res