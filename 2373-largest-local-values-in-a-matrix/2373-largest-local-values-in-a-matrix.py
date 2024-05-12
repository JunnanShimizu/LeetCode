class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = [[0]*(len(grid) - 2) for i in range(len(grid) - 2)]
        
        for i in range(0, len(grid) - 2):
            for j in range(0, len(grid) - 2):
                max_val = grid[i + 1][j + 1]
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        max_val = max(max_val, grid[x][y])
                        
                res[i][j] = max_val
                
        return res