def smallerNumbersThanCurrent(nums):
    many = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[i] > nums[j]:
                count +=1
        many.append(count)
        
    return many
nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))
