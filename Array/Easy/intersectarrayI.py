from collections import Counter

def intersection(nums1, nums2):
    count = Counter(nums1)

    curr = {}

    for n in nums2:
        curr[n] = curr.get(n, 0) + 1

    
    res = []
    for n in count:
        if n in curr:
            res.append(n)

    return res 
nums1 = [4, 9, 5]
nums2 = [9,4,9,8,4]

print(intersection(nums1, nums2))