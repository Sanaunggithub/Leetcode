def smallerThanCurrent(nums):
    many = []
    count = 0

    for right in range(len(nums)):
        for i in range(right, len(nums)):
            if nums[right] > nums[i]:
                count += 1
        
        many.append(count)


    return count

nums = [8,1,2,2,3]
print(smallerThanCurrent(nums))