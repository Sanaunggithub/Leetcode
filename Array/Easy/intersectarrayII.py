from collections import Counter

def intersect(nums1, nums2):
    count = Counter(nums1)
    curr = {}

    # first create a dict for num2
    for n in nums2:
        curr[n] = curr.get(n, 0) + 1

    res = []
    
    # finding intersection
    for n in count:
        if n in curr:       
            for i in range(min(count[n], curr[n])):
                res.append(n)
    return res

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersect(nums1, nums2))