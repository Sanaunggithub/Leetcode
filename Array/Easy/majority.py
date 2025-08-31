def majorityElement(nums):
    size = len(nums) // 2

    count = {}
    max = 0

    for i in range(len(nums)):
        count[nums[i]] = 1 + count.get(nums[i], 0)


    for k, v in count.items():
        if v > size:
            max = k
    return max
    
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))