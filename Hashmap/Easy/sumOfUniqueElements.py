def sumOfUnique(nums):
    h = {}
    sum = 0
    for n in nums:
        h[n] = h.get(n, 0) + 1

    for k in h:
        if h[k] == 1:
            sum += k

    return sum

nums = [1,2,3,2]
print(sumOfUnique(nums))