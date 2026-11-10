class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0

        for R in range(len(prices)):
            if prices[L] < prices[R]:
                res = max(res, prices[R] - prices[L])
            else:
                L = R
        return res
                