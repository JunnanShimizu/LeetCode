class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dictionary = {}
        
        for w in arr:
            dictionary[w] = dictionary.get(w, 0) + 1
            
        count = 0
        for v in dictionary:
            if dictionary[v] == 1:
                count += 1
                if count == k:
                    return v
        
        return ""