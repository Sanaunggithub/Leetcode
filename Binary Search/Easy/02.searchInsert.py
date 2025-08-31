def searchInsert(nums, target):
    

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        elif nums[mid] < target:
            left = mid + 1
        
        elif nums[mid] > target:
            right = mid - 1

    return left
        
    
nums = [1,3,5,6]
print(searchInsert(nums, 2))

"""
Eventually, when left <= right, the loop exits.

At that point:

left is the smallest index where the target could go

right is the largest index less than the target
"""