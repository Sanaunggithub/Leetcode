def rotate(nums, k):
    
    lst = []
    n = len(nums)
    right = len(nums) - 1

    k = k % len(nums)

    count = 0

    while count != k:
        lst.append(nums[right])
        count += 1
        right -= 1

    lst = lst[::-1]

    # -1 is used here because it is exclusive. will stop at 0.
    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]

    
    for i in range(k):
        nums[i] = lst[i]
    

    return nums

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums, k))

# | Iteration | i | Action                                  | nums after assignment   |
# | --------- | - | --------------------------------------- | ----------------------- |
# | 1         | 3 | `nums[3 + 3] = nums[3]` → `nums[6] = 4` | `[1, 2, 3, 4, 5, 6, 4]` |
# | 2         | 2 | `nums[2 + 3] = nums[2]` → `nums[5] = 3` | `[1, 2, 3, 4, 5, 3, 4]` |
# | 3         | 1 | `nums[1 + 3] = nums[1]` → `nums[4] = 2` | `[1, 2, 3, 4, 2, 3, 4]` |
# | 4         | 0 | `nums[0 + 3] = nums[0]` → `nums[3] = 1` | `[1, 2, 3, 1, 2, 3, 4]` |


# nums[:] = nums[-k:] + nums[:-k]

# nums[-k:] — grabs the last k elements of the list. [5, 6, 7]
# nums[:-k] — grabs everything before those last k elements. [1, 2, 3, 4]

# nums[:] means: assign to all elements of the original list in-place.

# nums = [1,  2,  3,  4,  5,  6,  7]
# index: 0   1   2   3   4   5   6
# neg:  -7  -6  -5  -4  -3  -2  -1

# nums[-3:] means start at -3 and go to end
# nums[:-3] means take everything before -3
