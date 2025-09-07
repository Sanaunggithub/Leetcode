def kidsWithCandies(candies, extraCandies):
    current_max = max(candies)

    res = []

    for candy in candies:
        if candy + extraCandies >= current_max:
            res.append(True)

        else:
            res.append(False)

    return res

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))