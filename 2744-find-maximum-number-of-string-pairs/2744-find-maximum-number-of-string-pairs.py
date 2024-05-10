class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int: 
        count = 0
        
        for i, w in enumerate(words):
            if w[::-1] in words and words.index(w[::-1]) != i:
                count += 1
                
        return int(count / 2)
            
        