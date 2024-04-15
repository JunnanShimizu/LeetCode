class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        sortNums = nums.sort()
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False