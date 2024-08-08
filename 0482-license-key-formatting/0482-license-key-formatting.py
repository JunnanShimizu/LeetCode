class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        noDashes = ""
        
        for c in s:
            if c != '-':
                noDashes += c

        subs = []
        r = len(noDashes)
        l = r - k
        while l > 0:
            subs.append(noDashes[l:r])
            r -= k
            l -= k
        
        subs.append(noDashes[0:r])
        
        print(subs)
        
        res = ""
        for i in range(len(subs) - 1, -1, -1):
            res += subs[i].upper()
            if i != 0:
                res += '-'
            
        return res
                 
        
        
                
        
                
        
        
            