def generate(numRows):
        
    res = [[1]]

    for i in range(numRows - 1): # 1 row is already taken in the above
        tmp = [0] + res[-1] + [0] 
        row = []
        for j in range(len(res[-1]) + 1): # prev row plus one 
            row.append(tmp[j] + tmp[j + 1]) # adding above values
        
        res.append(row)

    return res