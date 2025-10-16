def sortPeople( names, heights):
        
    # zip() takes two or more iterables (like lists, tuples, strings) and pairs their elements together into tuples.
    
    pairs = list(zip(names, heights)) # [('Alice', 155), ('Bob', 185), ('Charlie', 170)]

    # items() return tuple = (key, value)
    # x[0] = "Mary" x[1]= 180
    # sorted returns a new list

    sorted_pairs = sorted(pairs, key= lambda x:x[1] ,reverse=True)

    res = []

    for name, _ in sorted_pairs:
        res.append(name)

    return res
    
names = ["Mary","John","Emma"]
heights = [180,165,170]

print(sortPeople(names, heights))