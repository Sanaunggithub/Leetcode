def runningSum(nums):
    res = []
    sum = 0
    for num in nums:
        sum += num
        res.append(sum)
    return res
nums = [1,1,1,1,1]
print(runningSum(nums))