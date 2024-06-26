class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        max_length = 0
        
        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                max_length = max(max_length, r - l + 1)
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
            
        return max_length
            
                
        
        