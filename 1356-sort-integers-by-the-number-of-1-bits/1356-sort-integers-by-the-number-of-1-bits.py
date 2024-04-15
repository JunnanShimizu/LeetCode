class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        arr.sort(key = lambda x: (bin(x).count('1'), x))
        return arr