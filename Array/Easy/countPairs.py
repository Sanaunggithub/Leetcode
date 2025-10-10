def countPairs(nums, target):
    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i, n):
            if i != j and nums[i] + nums[j] < target:
                count += 1

    return count

nums = [-1,1,2,3,1]
target = 2
print(countPairs(nums, target))