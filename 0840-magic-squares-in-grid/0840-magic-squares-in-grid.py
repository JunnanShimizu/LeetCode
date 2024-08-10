class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        def isMagicSquare(r, c): #r, c being the center coords
            topL = grid[r - 1][c - 1]
            topM = grid[r - 1][c]
            topR = grid[r - 1][c + 1]
            
            midL = grid[r][c - 1]
            midM = grid[r][c]
            midR = grid[r][c + 1]
            
            botL = grid[r + 1][c - 1]
            botM = grid[r + 1][c]
            botR = grid[r + 1][c + 1]
            
            vals = [topL, topM, topR, midL, midM, midR, botL, botM, botR]
            uniques = {}
            for v in vals:
                if v < 1 or v > 9:
                    return False
                uniques[v] = uniques.get(v, 0) + 1
                if uniques[v] == 2:
                    return False
                
            topRow = topL + topM + topR
            midRow = midL + midM + midR
            botRow = botL + botM + botR
            
            
            lCol = topL + midL + botL
            mCol = topM + midM + botM
            rCol = topR + midR + botR
            
            lrDiag = topL + midM + botR
            rlDiag = topR + midM + botL
            
            if topRow == midRow == botRow == lCol == mCol == rCol == lrDiag == rlDiag:
                return True
            else:
                return False
        
        count = 0
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):
                if isMagicSquare(r, c):
                    count += 1
                    
        return count
                    