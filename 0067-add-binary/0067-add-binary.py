class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_sum = int(a, 2) + int(b, 2)
        
        return str(bin(bin_sum))[2:]