def shuffle(nums, n):

    l1 = nums[:n]
    l2 = nums[n:]

    
    res = []
    for i in range(len(l1)):
        res.append(l1[i])
        res.append(l2[i])

    return res



nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums,n))