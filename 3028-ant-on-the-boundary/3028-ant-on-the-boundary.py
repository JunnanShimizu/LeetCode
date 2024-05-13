class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        location = 0
        count = 0
        
        for n in nums:
            location += n
            if location == 0:
                count += 1
        
        return count