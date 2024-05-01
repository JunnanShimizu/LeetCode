class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0: 
            negative = True
            x *= -1
            
        strx = str(x)[::-1]
        
        if(negative):
            strx = "-" + strx
            
        if int(strx) >= 2**31 - 1 or int(strx) <= -(2**31):
            return 0
        else:
            return int(strx)
        
        