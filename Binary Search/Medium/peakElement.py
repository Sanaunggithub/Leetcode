def findPeakElement(self, nums):
        
    def findPeak(nums , l, h):
        if l > h: return 0

        mid = (l + h) // 2

        left = nums[mid - 1] if mid > 0 else float('-inf') # negative infinity
        right = nums[mid + 1] if mid < len(nums) - 1 else float('-inf') # positive infinity

        if left < nums[mid] and nums[mid] > right:
            return mid

        elif left < nums[mid] < right:
            return findPeak(nums, mid + 1, h)

        else:
            return findPeak(nums, l, mid - 1)

    return findPeak(nums, 1, len(nums)-1)