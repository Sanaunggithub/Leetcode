def searchRange(nums, target):
    
    def search(nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1

            elif target < nums[m]:
                r = m - 1

            else:
                i = m # save the position
                if leftBias:
                    r = m - 1

                else:
                    l = m + 1

        return i
    left = search(nums, target, True)
    right = search(nums, target, False)

    return [left, right]



