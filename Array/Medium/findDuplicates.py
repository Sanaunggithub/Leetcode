def findDuplicates(nums):
    lst = []

    seen = set()
    for n in nums:
        if n not in seen:
            seen.add(n)

        else:
            lst.append(n)

    return lst