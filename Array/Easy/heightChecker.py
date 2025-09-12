def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Make a sorted copy of the heights
        expected = sorted(heights)
        
        # Count the number of positions where heights differ from expected
        count = 0
        for h, e in zip(heights, expected):
            if h != e:
                count += 1
        
        return count