def numWaterBottles(numBottles, numExchange):
    emptyBottle = 0
    drank = 0

    while numBottles > 0:
        drank += numBottles
        emptyBottle += numBottles

        numBottles = emptyBottle // numExchange
        emptyBottle = emptyBottle % numExchange  

    return drank 

numBottles = 15
numExchange = 4
print(numWaterBottles(numBottles, numExchange))