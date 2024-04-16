class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rset = {}
        mset = {}
        
        for c in ransomNote:
            rset[c] = 1 + rset.get(c, 0)
            
        for c in magazine:
            mset[c] = 1 + mset.get(c, 0)
            
        for k in rset.keys():
            if mset.get(k) == None or mset.get(k) < rset.get(k):
                return False
            
        return True
            