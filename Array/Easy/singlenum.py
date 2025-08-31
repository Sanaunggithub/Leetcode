def singleNumber(nums):
    seen = {}

    for i in range(len(nums)):
        seen[nums[i]] = seen.get(nums[i], 0) + 1
        
    print(seen)
    for k in seen:
        if seen[k] == 1:
            return k
        
nums = [2,2,1]
print(singleNumber(nums))

# # If there's only one element, return it directly
# if len(nums) == 1:
#     return nums[0]

# # Initialize result to 0
# result = 0

# # XOR all numbers: duplicates cancel out, leaving the unique number
# for i in nums:
#     result ^= i

# # Return the unique number
# return result
