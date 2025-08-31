def containsNearbyDuplicate(nums, k):
    window = set()
    left = 0

    for right in range(len(nums)):
        # if window size is big, shrink the lefct
        if right - left > k:
            window.remove(nums[left])
            left += 1


        
        if nums[right] in window:
            return True
        
        window.add(nums[right])

    return False

nums = [1,2,3,1]
k = 3