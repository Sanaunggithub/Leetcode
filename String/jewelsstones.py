def numJewelsInStones(jewels, stones):
    count = 0
    jewels = set(jewels)
    
    for stone in stones:
        if stone in jewels:
            count += 1
    return count


jewels = "aA"
stones = "aAAbbbb"

print(numJewelsInStones(jewels, stones))