class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for i, c in enumerate(strs[0]):
            for w in strs:
                if i >= len(w) or w[i] != c:
                    return res
            res += c
            
        return res