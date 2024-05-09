class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            isSDN = True
            for c in str(i):
                if c == "0" or i % int(c) != 0:
                    isSDN = False
            if isSDN == True:
                res.append(i)
                
        return res