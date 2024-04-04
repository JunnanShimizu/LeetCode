class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        candies = [1] * len(ratings)
        des = [0] * len(ratings)

        fsum = 0

        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                des[i - 1] = des[i] + 1
        
        candies[0] = des[0] + 1

        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                if des[i + 1] <= candies[i]:
                    candies[i + 1] = candies[i] + 1
                else: # des[i + 1] > candies[i]
                    candies[i + 1] = des[i + 1] + 1
            elif ratings[i] > ratings[i + 1]:
                candies[i + 1] = des[i + 1] + 1
            else: # ratings[i] == ratings[i + 1]
                if des[i + 1] == 0:
                    candies[i + 1] = 1
                else: # des[i + 1] > 0
                    candies[i + 1] = des[i + 1] + 1
                   
        for n in candies:
            fsum += n

        return fsum