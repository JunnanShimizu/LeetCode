class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        l = 0
        for i in range(len(s)):
            if i == 0:
                continue
            if s[i] in s[l:i]:
                count += 1
                l = i

        return count
        

        