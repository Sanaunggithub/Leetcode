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

# Array: [0,2,3]

# last_index = 2

# max_reachable = 0 initially

# Step 1: i = 0

# nums[i] = 0 → i + nums[i] = 0 + 0 = 0

# Update max_reachable = max(0, 0) = 0

# Check: i > max_reachable? → 0 > 0 → False (okay, still reachable)

# Check: max_reachable >= last_index? → 0 >= 2 → False (not reached yet)

# ✅ Output so far:

# i=0, nums[i]=0, max_reachable=0

# Step 2: i = 1

# i > max_reachable? → 1 > 0 → True

# We are stuck! Index 1 is unreachable because max_reachable = 0 → can’t move past index 0

# ✅ Algorithm returns False immediately.
