class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        cache = {}

        rows = len(matrix)
        cols = len(matrix[0])

        def helper(r, c): 
            if r >= rows or c >= cols:
                return 0
            
            if (r, c) not in cache:
                right = helper(r, c + 1)
                below = helper(r + 1, c)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(right, below, diag)
            
            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2