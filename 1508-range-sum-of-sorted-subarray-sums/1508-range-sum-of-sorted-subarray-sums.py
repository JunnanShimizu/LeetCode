class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new_nums = []
        
        for s in range(n + 1):
            for e in range(s + 1, n + 1):
                new_nums.append(sum(nums[s:e]))
                    
        new_nums.sort()
                        
        return (sum(new_nums[left - 1:right]) % (10**9 + 7))
                    
        
            
        
                
                
                