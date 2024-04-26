from heapq import heapify, heappush, heappop 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)
        
        for (x, y) in points:
            dist = sqrt(x**2 + y**2)
            heappush(heap, (dist, x, y))
            
        res = []
        for i in range(k):
            cur = heappop(heap)
            res.append([cur[1], cur[2]])
            
        return res
        
        
            
        