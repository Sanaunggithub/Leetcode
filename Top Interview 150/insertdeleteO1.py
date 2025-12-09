class RandomizedSet(object):

    def __init__(self):
        self.numMap = {}
        self.numList = []
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val not in self.numMap

        if res:
           self.numMap[val] = len(self.numList)
           self.numList.append(val)
        return res

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val in self.numMap

        if res:
            index = self.numMap[val]
            lastValue = self.numList[-1]
            self.numList[index] = lastValue
            self.numList.pop()
            self.numMap[lastValue] = index
            del self.numMap[val]
        
        return res
    def getRandom(self):
        """
        :rtype: int
        """
        
        return random.choice(self.numList)