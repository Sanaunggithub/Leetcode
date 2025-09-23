def compareVersion(version1, version2):

    v1 = version1.split(".")
    v2 = version2.split(".")

    i1 = [int(v) for v in v1]
    i2 = [int(v) for v in v2]

    for i in range(max(len(i1), len(i2))):
        num1 = (i1[i] if i < len(i1) else 0)
        num2 = (i2[i] if i < len(i2) else 0)

        if num1 > num2:
            return 1
        
        elif num1 < num2:
            return -1
        
    return 0


version1 = "1.01"
version2 = "1.001"
print(compareVersion(version1, version2))
