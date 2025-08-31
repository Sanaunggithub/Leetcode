def distinctAverages(nums):

    lst = []

    while len(nums) > 0:
        s = min(nums)
        b = max(nums)
        avg = (s + b) / 2

        nums.remove(s)
        nums.remove(b)

        if avg not in lst:
            lst.append(avg)

    return len(lst)





nums = [9,5,7,8,7,9,8,2,0,7]
print(distinctAverages(nums))