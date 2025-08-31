def uniqueOccurrences(arr):

    h = {}
    lst = []
    for a in arr:
        h[a] = h.get(a, 0) + 1

    for k,v in h.items():
        if v in lst:
            return False
        lst.append(v)
    
    return True
    
    
arr = [1,2]
print(uniqueOccurrences(arr))