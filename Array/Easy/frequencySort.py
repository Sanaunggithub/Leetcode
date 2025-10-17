def frequencySort(nums):
    h = {}

    for i in range(len(nums)):
        h[nums[i]] = h.get(nums[i], 0) + 1

    d = list(sorted(h.items(), key=lambda x: (x[1], -x[0])))
    
    res = []
    for p in d:
        for i in range(p[1]):
            res.append(p[0])

    return res
nums = [1,1,2,2,2,3]
print(frequencySort(nums))