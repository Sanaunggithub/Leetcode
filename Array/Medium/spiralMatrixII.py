class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]

        left, right = 0, n 
        top, bottom = 0, n 
        num = 1

        while top < bottom and left < right:
            tmp = []
            # get every i in top row
            for i in range(left, right):
                res[top][i]= num
                num += 1
            top += 1

            # get every i in right col
            for i in range(top, bottom):
                res[i][right -1 ] = num
                num += 1
            right -= 1

            if not (top < bottom and left < right):
                break

            # get every i in bottom row:
            for i in range(right -1, left -1 , -1):
                res[bottom -1][i] = num
                num += 1
            bottom -= 1
            
            # get every i in left col:
            for i in range(bottom -1 , top -1, -1):
                res[i][left] = num
                num += 1
            left += 1

        return res