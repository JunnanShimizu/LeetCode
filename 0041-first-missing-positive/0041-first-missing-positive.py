class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)

        for i in range(l):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(l):
            val = abs(nums[i])
            if 1 <= val <= l:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (l + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return l + 1