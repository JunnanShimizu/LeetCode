class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        maxProfit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                if maxProfit < p - min_price:
                    maxProfit = p - min_price

        return maxProfit