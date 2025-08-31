def removeDuplicates(nums):

    l = 1
    count = 1

    for r in range(1, len(nums)):

        if nums[r] != nums[r-1]:
            count = 0
        
        if count < 2:
            nums[l] = nums[r]
            l += 1
            count += 1

    
    return l 

nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))






            

                 