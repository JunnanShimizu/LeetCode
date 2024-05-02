class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set()
        max_num = -1
        
        for n in nums:
            if (-1 * n) in num_set:
                max_num = max(max_num, abs(n))
            num_set.add(n)
        
        return max_num
        