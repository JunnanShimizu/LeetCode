class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        eng = []
        for eff, spd in zip(efficiency, speed):
            eng.append([eff, spd])

        eng.sort(reverse=True)

        res = 0
        tspd = 0

        minHeap = []
        for eff, spd in eng:
            if len(minHeap) == k:
                tspd -= heapq.heappop(minHeap)
            tspd += spd
            heapq.heappush(minHeap, spd)
            res = max(res, eff * tspd)

        return res % (10**9 + 7)