class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        
        res = []

        if rounds[0] == rounds[-1]:
            return [rounds[0]]
        elif rounds[0] < rounds[-1]:
            for i in range(rounds[0], rounds[-1] + 1):
                res.append(i)
            return res
        else: # rounds[0] > rounds[-1]
            cur = rounds[0]
            while cur != rounds[-1]:
                res.append(cur)
                cur += 1
                if cur > n:
                    cur = 1
            res.append(rounds[-1])
            res.sort()
            return res
            
