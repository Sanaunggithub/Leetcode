def alternatingSum(nums):
    if len(nums) == 1:
        return nums[0]

    res = nums[0] 

    for i in range(1, len(nums)):
        print(res)
        if i % 2 == 0:
            res += nums[i]

        
        else:
            res -=  nums[i]

    return res 

nums = [1,3,5,7]
print(alternatingSum(nums))
