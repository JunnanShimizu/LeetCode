class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = {}
    
        for c in s:
            chars[c] = 1 + chars.get(c, 0)
            
        even_chars = 0
        add_odd = False
        for v in chars.values():
            if not add_odd and v % 2 == 1:
                even_chars += 1
                add_odd = True
            if v > 1 and v % 2 == 0:
                even_chars += v 
            elif v > 1 and v % 2 == 1:
                even_chars += v - 1
                
        return even_chars