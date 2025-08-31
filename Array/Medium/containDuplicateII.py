def containsNearbyDuplicate(nums, k):

    window = set()
    left = 0

    for right in range(len(nums)):
        if right - left > k:
            window.remove(nums[left])
            left += 1

        if nums[right] in window:
            return True
        
        window.add(nums[right])

    return False

nums = [1,2,3,1,2,3]
k = 1

print(containsNearbyDuplicate(nums, k))



# dic = {}
# for i, num in enumerate(nums):
#     if num in dic and i - dic[num] <= k:
#         return True
#     dic[num] = i
# return False 