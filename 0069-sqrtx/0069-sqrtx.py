class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        
        while res * res < x:
            res += 1
            
        if res * res > x:
            return res - 1
            
        return res
            
            