import numpy as np

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        res = 0
        for r in range(len(grid)):
            if grid[r][0] == 0:
                for c in range(len(grid[r])):
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                    else:
                        grid[r][c] = 0
                
        for c in range(len(grid[0])):
            zero_count = 0
            for r in range(len(grid)):
                if grid[r][c] == 0:
                    zero_count += 1
                                
            if zero_count > len(grid) - zero_count:
                for r in range(len(grid)):
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                    else:
                        grid[r][c] = 0
                        
        res = 0    
            
        for r in grid:
            string = ""
            for v in r:
                string += str(v)
                
            res += int(string, 2)
        
        return res
                 