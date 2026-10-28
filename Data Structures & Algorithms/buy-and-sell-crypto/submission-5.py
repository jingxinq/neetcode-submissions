class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        res = 0
        for sell in range(len(prices)):  
            if prices[sell]-prices[buy] > 0:
                res = max(res, prices[sell]-prices[buy])
            elif prices[sell]-prices[buy] < 0:
                buy = sell

        return res
