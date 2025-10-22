def distributeCandies(candyType):  
    s = set()

    for c in candyType:
        s.add(c)

    allowed = len(candyType) // 2
    type = len(s) 

    return min(allowed, type)

candyType = [1,1,2,2,3,3]

print(distributeCandies(candyType))