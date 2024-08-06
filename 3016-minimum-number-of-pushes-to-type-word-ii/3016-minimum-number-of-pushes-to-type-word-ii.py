class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = {}
        
        for c in word:
            counts[c] = counts.get(c, 0) + 1
            
        if len(counts.keys()) < 8:
            return len(word)
        
        heap = []
        heapify(heap)
        
        for v in counts.values():
            heappush(heap, -v)
        
        count = 0
        res = 0
        while heap:
            val = -heappop(heap)
            count += 1
            if count % 8 == 0:
                res += count // 8 * val
            else:
                res += ((count // 8) + 1) * val
            
        return res
            
            
            
            
            
                
            
        
                
                