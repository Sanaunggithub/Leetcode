def targetIndices(nums, target):
     
    nums.sort()
    res = []

    for i in range(len(nums)):
        if target == nums[i]:
            res.append(i)

    return res