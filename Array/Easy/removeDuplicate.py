def removeDuplicates(nums):
    
    left = 0

    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1

    return left


nums =  [2,10,10,30,30,30]
print(removeDuplicates(nums))