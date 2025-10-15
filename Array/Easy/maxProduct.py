def maxProduct(nums):
    a=max(nums)
    nums.remove(a)
    b=max(nums)
    return (a-1)*(b-1)


nums = [1,5,4,5]
print(maxProduct(nums))