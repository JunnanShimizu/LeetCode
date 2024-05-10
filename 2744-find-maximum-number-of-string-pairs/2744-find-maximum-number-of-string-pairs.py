class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int: 
        count = 0
        
        for w in words:
            if w[::-1] in words and words.index(w[::-1]) != words.index(w):
                count += 1
                
        return int(count / 2)
            
        