class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        solutions = []
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            r = len(nums) - 1
            l = i + 1
            while r > l:
                threeSum = nums[l] + nums[r] + n
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    solutions.append([nums[l], nums[r], n])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return solutions