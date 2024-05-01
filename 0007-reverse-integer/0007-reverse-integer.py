class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        new_string = ""
        negative = False
        
        for i in range(len(strx) - 1, -1, -1):
            if strx[i] == "-":
                negative = True
            else:
                new_string += strx[i]
                
        if negative:
            new_string = "-" + new_string
            
        if int(new_string) >= 2**31 - 1 or int(new_string) <= -(2**31):
            return 0
        else:
            return int(new_string)