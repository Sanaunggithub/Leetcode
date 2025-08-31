def maxProfit(prices):
    left = 0
    max_profit = 0

    for right in range(1, len(prices)):
        # profitable ?
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

        else:
            left = right # becuz right will hold the lowest price so far
    print(max_profit)

prices = [7,1,5,3,6,4]
maxProfit(prices)


# buy = prices[0]
# profit = 0
# for i in range(1, len(prices)):
#         buy = prices[i]
#     elif prices[i] - buy > profit:
#         profit = prices[i] - buy
# return profit