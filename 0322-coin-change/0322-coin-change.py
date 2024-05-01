class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for n in range(1, amount + 1):
            for c in coins:
                if n - c >= 0:
                    dp[n] = min(dp[n], 1 + dp[n - c])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1