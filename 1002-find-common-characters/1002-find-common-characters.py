class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dicts = []
        
        for i in range(len(words)):
            count = {}
            for c in words[i]:
                count[c] = count.get(c, 0) + 1
            dicts.append(count)
        
        res = []
                
        for k in dicts[0].keys():
            min_count = dicts[0][k]
            for d in dicts:
                min_count = min(min_count, d.get(k, 0))
            if min_count > 0:
                for i in range(min_count):
                    res.append(k)
        
        return res
                
            
        