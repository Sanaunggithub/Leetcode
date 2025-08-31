def twoSum(nums, target):
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in prevMap:
            return [prevMap[diff], i]
        
        prevMap[n] = i

nums = [2,7,11,15]

print(twoSum(nums, 9))


# Hashmap - dict
# val : index