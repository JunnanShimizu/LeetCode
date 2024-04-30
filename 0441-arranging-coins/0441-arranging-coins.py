class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        level = 1
        
        while n > 0:
            n -= level
            level += 1
            if n >= 0:
                count += 1
            
        return count
            