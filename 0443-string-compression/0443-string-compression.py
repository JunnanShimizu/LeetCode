class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        :type chars: List[str]
        :rtype: int
        """

        count = 1
        res = ""

        if len(chars) == 1:
            return 1

        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                if count == 1:
                    res = res + str(chars[i])
                else:
                    res = res + str(chars[i]) + str(count)
                    count = 1
            if i == (len(chars) - 2):
                if count == 1:
                    res = res + str(chars[i + 1])
                else:
                    res = res + str(chars[i + 1]) + str(count)
                    count = 1

        for i, c in enumerate(res):
            chars[i] = c

        return len(res)
                