def missingNumber(nums):
    for _ in range(len(nums) + 1):
        if _ not in nums:
            return _
    

nums = [3,0,1]
print(missingNumber(nums))

# bitwise manipulation
# def missingNumber(nums):
#         n = len(nums)
#         ans = 0
#         for i in range(1, n + 1):
#             ans ^= i
#         for num in nums:
#             ans ^= num
#         return ans

# i = 1 → ans = 0 ^ 1 = 1

# i = 2 → ans = 1 ^ 2 = 3

# i = 3 → ans = 3 ^ 3 = 0

# num = 3 → ans = 0 ^ 3 = 3

# num = 0 → ans = 3 ^ 0 = 3

# num = 1 → ans = 3 ^ 1 = 2
