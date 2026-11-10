class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        L = 0
        res = 0

        for R in range(L + 1, len(prices)):
            if prices[R] > prices[L]:
                res = max(res, prices[R] - prices[L])
            else:
                L = R # lower price found 
        return res