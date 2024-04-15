class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        """
        :type names: List[str]
        :rtype: List[str]
        """

        count = {}
        
        for i, n in enumerate(names):
            count[n] = 1 + count.get(n, 0)
            if count[n] > 1:
                k = count[n] - 1
                while n +  "(" + str(k) + ")" in count:
                    k += 1
                names[i] = names[i] + "(" + str(k) + ")"
                count[names[i]] = 1
                
                
        return names