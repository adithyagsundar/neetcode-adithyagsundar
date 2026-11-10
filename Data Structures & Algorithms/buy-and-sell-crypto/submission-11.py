class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        sliding window
        if a greater price is found then what is currently the bottom, we update res
        if a lower price is found then what currently is the lowest, update the lowest price to that price, thus L = R
        """
        L = 0
        res = 0

        for R in range(L + 1, len(prices)):
            if prices[R] > prices[L]:
                res = max(res, prices[R] - prices[L])
            else:
                L = R # lower price found 
        return res