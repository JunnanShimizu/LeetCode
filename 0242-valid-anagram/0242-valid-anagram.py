class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_chars = list(s)
        t_chars = list(t)

        s_chars.sort()
        t_chars.sort()

        if s_chars == t_chars:
            return True
        else:
            return False