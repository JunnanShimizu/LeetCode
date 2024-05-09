class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        
        for i, n in enumerate(happiness):
            if n - i > 0 and k > 0:
                res += n - i
                k -= 1
            
        return res
            
        
        
        
        