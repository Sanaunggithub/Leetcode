def findThePrefixCommonArray(A, B):
    frequency = {}
    res = [0] * len(A)
    common = 0

    for i in range(len(A)):

        frequency[A[i]] = frequency.get(A[i], 0) + 1

        if frequency[A[i]] == 2:
            common += 1
        
        frequency[B[i]] = frequency.get(B[i], 0) + 1

        if frequency[B[i]] == 2:
            common += 1

        res[i] = common
    return res

    
A = [1,3,2,4]
B = [3,1,2,4]

print(findThePrefixCommonArray(A, B))