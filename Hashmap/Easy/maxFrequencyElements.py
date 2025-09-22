def maxFrequencyElements(nums):

    f = {}

    for n in nums:
        f[n] = f.get(n ,0) + 1

    max_key = max(f.values())
    
    total = 0

    for k, v in f.items():
        if v == max_key:
            total += v


    return total

nums = [1,2,2,3,1,4]
print(maxFrequencyElements(nums))