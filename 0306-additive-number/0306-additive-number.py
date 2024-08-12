class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        def isAdditive(first, second, remainder):
            print(first, second, remainder)
            if len(remainder) < max(len(first), len(second)):
                return False
            
            if (first[0] == '0' and len(first) != 1) or (second[0] == '0' and len(second) != 1):
                return False
            
            total = str(int(first) + int(second))
            if len(total) > len(remainder):
                return False
            
            if total == remainder[0:len(total)]:
                if len(remainder) == len(total):
                    return True
                return isAdditive(second, remainder[0:len(total)], remainder[len(total):])
            
            return False
    
        for i in range(1, len(num)):
            for i2 in range(1, len(num)):
                if isAdditive(num[:i], num[i:i + i2], num[i + i2:]):
                    return True
                
        return False
                
                