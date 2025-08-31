def isUgly(n):
    if n < 1:
        return False
    
    f = [2, 3, 5]
    
    for i in range(len(f)):
        while n % f[i] == 0:
            n = n // f[i] # i will not increment here

        # i will be incremented here 
    return n == 1

print(isUgly(1))