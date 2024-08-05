class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        if len(digits) == 0:
            return []
        
        dictionary = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        
        def backtrack(idx, string):
            if len(digits) == idx:
                res.append(string)
                return
            for c in dictionary[int(digits[idx])]:
                backtrack(idx + 1, string + c)
                
        
        backtrack(0, "")
        return res
        
                
            