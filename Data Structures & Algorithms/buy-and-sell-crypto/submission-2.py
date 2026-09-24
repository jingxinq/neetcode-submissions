class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low sell high
        res = 0
        L = 0 # L is buy, R is sell

        for R in range(1, len(prices)):
            if prices[R] > prices[L]:
                res = max(res, prices[R]-prices[L])
            else: 
                L = R

        return res
