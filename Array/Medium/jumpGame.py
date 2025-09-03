def canJump(nums):
    last = len(nums) - 1
    
    max_reachable = 0

    for i in range(len(nums)):
        if i > max_reachable:
            return False
        
        max_reachable = max(max_reachable, i + nums[i])

        if max_reachable >= last:
            return True
        
    return False

        
        
nums = [0,2,3]
print(canJump(nums))
