class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_nums = {}
        
        for n in nums:
            num_nums[n] = 1 + num_nums.get(n, 0)
            
        for k, v in num_nums.items():
            if v > len(nums) / 2:
                return k
            
        return -1