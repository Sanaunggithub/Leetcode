def maximumWealth(accounts):
    wealth = []

    for account in accounts:
        sum = 0
        for money in account:
            sum += money

        wealth.append(sum)

    return max(wealth)


accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))
