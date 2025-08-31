def sortedSquares(nums):

    res = []
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            res.append(nums[left] * nums[left])
            left += 1

        else:
            res.append(nums[right] * nums[right])
            right -= 1

    return res[::-1] # reverse the array
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))