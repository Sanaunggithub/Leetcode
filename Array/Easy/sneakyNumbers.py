def getSneakyNumbers(nums):
    seen = []
    res = []

    for n in nums:
        if n not in seen:
            seen.append(n)

        else:
            res.append(n)
    return res