def maximumCount(nums):
    pcount = 0
    ncount = 0

    for i in nums:
        if i == 0:
            continue
            
        elif i < 0:
            ncount += 1
        
        else:
            pcount +=1
    
    return max(pcount, ncount)
            

nums = [-2,-1,-1,1,2,3]
print(maximumCount(nums))


# import bisect

# def maximumCount(nums):
#     # Find first index of 0 or greater
#     first_non_negative = bisect.bisect_left(nums, 0)
    
#     # Find first index of number greater than 0
#     first_positive = bisect.bisect_right(nums, 0)
    
#     # Count negatives = everything before first non-negative
#     negative_count = first_non_negative
    
#     # Count positives = everything after last 0
#     positive_count = len(nums) - first_positive

#     return max(negative_count, positive_count)