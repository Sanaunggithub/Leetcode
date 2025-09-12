def heightChecker(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)

        res = []

        i = 0

        while i < len(heights):
                if heights[i] != expected[i]:
                        res.append(heights[i])
                i += 1
        return len(res)

heights = [1,1,4,2,1,3]
print(heightChecker(heights))