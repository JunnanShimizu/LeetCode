class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = []
        
        for i in arr:
            for j in arr:
                if i != j and i < j:
                    res.append([i/j, i, j])
                    
        res.sort()
        
        return [res[k - 1][1], res[k - 1][2]]