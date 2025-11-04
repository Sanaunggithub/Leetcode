def countMatches(self, items, ruleKey, ruleValue):     
    res = 0
    
    if ruleKey == "type":
        ruleKey = 0
    
    elif ruleKey == "color":
        ruleKey = 1

    else:
        ruleKey = 2

    res = 0
    for item in items:
        i = item[ruleKey]

        if i == ruleValue:
            res += 1

    return res
