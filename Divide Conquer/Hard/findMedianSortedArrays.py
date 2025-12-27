def findMedianSortedArrays(nums1, nums2):
    
    nums1.extend(nums2)
    nums1.sort()

    even = len(nums1) // 2 == 0
    return nums1[mid]

nums1 = [1,3]
nums2 = [2,4]
print(findMedianSortedArrays(nums1, nums2))