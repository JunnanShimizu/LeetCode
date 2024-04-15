class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        new_s = []
        new_t = []

        for c in s:
            if c != "#":
                new_s.append(c)
            else:
                if new_s:
                    new_s.pop()

        for c in t:
            if c != "#":
                new_t.append(c)
            else:
                if new_t:
                    new_t.pop()

        if new_s == new_t:
            return True