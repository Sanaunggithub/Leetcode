import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        min_heap = []

        # push first element of each row
        for i, row in enumerate(matrix):
            heapq.heappush(min_heap, (row[0], i, 0))

        count = 0

        while min_heap:
            value, i, j = heapq.heappop(min_heap)
            count += 1

            if count == k:
                return value

            # push next element from the same row
            if j + 1 < len(matrix[i]):
                heapq.heappush(min_heap, (matrix[i][j+1], i, j+1))