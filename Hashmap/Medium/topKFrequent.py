def topKFrequent(nums, k):
    
    count = {}

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    res = []
    
    vals = list(count.values())
    vals.sort(reverse=True) # sort greatest to smallest

    kth_freq = vals[k - 1] # [7, 5, 5, 3, 2, 1], k = 3


    for key, v in count.items():
        if v >= kth_freq:
            res.append(key)

    return res
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))