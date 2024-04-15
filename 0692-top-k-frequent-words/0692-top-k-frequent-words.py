class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        hashset = {}

        counts = [[] for i in range(len(words) + 1)] 

        for w in words:
            hashset[w] = 1 + hashset.get(w, 0)
                
        for n, c in hashset.items():
            counts[c].append(n)

        result = []
        for i in range(len(words) - 1, 0, -1):
            counts[i].sort()
            for w in counts[i]:
                result.append(w)
                if len(result) == k:
                    return result     