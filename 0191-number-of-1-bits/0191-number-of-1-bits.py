class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(bin(n)[2:])
        
        count = 0
        for c in binary:
            if c == '1':
                count += 1
        
        return count