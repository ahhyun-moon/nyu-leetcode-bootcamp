class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
            # max_profit = 0
            # for buy_at in range(len(prices)):
            #     for sell_at in range(buy_at + 1, len(prices)):
            #         profit = prices[sell_at] - prices[buy_at]
            #         if profit > max_profit:
            #             max_profit = profit
            # return max_profit
        # single scan
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit