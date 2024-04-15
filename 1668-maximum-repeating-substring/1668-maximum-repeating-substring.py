class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """

        res = 0
        og_word = word

        while word in sequence:
            res += 1
            word = word + og_word

        return res
            