class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        heap = []
        heapq.heapify(heap)
        
        for v in stones: 
            heapq.heappush(heap, -v)
        
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            
            if x == y:
                continue
            else:   
                remainder = y - x
                heapq.heappush(heap, -remainder)
                
        if len(heap) == 0:
            return 0
        else:
            return -heapq.heappop(heap)
            
        
        