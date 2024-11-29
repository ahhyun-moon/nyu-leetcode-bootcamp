class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-up (tabularization) DP
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        # def findNumCoin(amount, memo):
        #     if amount in memo:
        #         return memo[amount]
        #     if amount == 0:
        #         return 0
        #     elif amount < 0:
        #         return -1
        #     min_coin = float('inf')
        #     for coin in coins:
        #         result = findNumCoin(amount - coin, memo)
        #         if result != -1:
        #             min_coin = min(min_coin, result + 1)
        #     memo[amount] = min_coin if min_coin != float('inf') else -1
        #     return memo[amount]
        # return findNumCoin(amount, {})
            
        