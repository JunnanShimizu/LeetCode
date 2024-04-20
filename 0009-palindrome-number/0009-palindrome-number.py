class Solution:
    def isPalindrome(self, x: int) -> bool:
        p1 = 0
        p2 = len(str(x)) - 1
        
        x = str(x)
        
        while p1 <= p2:
            if x[p1] != x[p2]:
                return False
            p1 += 1
            p2 -= 1
            
        return True
                 
        