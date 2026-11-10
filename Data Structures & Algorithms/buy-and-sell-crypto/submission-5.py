class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0

        for R in range(len(prices)):
            while prices[R] > prices[L]:
                res = max(res, prices[R] - prices[L])
                L += 1
            L += 1
        return res
                