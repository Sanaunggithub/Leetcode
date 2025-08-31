def moveZeroes(nums):

    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums

nums = [1,0]

print(moveZeroes(nums))