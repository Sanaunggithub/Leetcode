def totalMoney(n):      
    res = 0
    for i in range(n):
        week = i // 7      # which week (0-indexed)
        day = i % 7        # which day in the week (0–6)
        res += week + day + 1  # deposit amount
    return res


n = 20
print(totalMoney(n))