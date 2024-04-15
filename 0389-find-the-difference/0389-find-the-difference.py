class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        s_hashset = {}
        t_hashset = {}

        for c in s:
            if c in s_hashset:
                s_hashset[c] += 1
            else:
                s_hashset[c] = 1
        
        for c in t:
            if c in t_hashset:
                t_hashset[c] += 1
            else:
                t_hashset[c] = 1

        for c in t:
            if c not in s_hashset:
                return c
            elif s_hashset[c] != t_hashset[c]:
                return c