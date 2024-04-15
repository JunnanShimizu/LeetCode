class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
        index = {}
        
        degree = 0
        min_len = 0

        for i, n in enumerate(nums):
            count[n] = 1 + count.get(n, 0)
            if n not in index:
                index[n] = i
            if count[n] > degree:
                degree = count[n] 
                min_len = i - index[n] + 1
            elif count[n] == degree:
                if min_len > i - index[n] + 1:
                    min_len = i - index[n] + 1
        
        return min_len