class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        for i , val in enumerate(prices):
            for j in range (0,i):
                res = max(res, val-prices[j])
        return res
