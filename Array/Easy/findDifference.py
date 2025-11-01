def findDifference( nums1, nums2):
        
    s1 = set()
    s2 = set()

    res = []

    for n in nums1:
        s1.add(n)

    for n in nums2:
        s2.add(n)

    d1 = list(s1 - s2)
    d2 = list(s2 - s1)

    res.append(d1)
    res.append(d2)

    return res

nums1 = [1,2,3]
nums2 = [2,4,6]

print(findDifference(nums1, nums2))