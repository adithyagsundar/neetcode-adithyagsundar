class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        we move the smaller height because it's the bottleneck
        we dont need to check everything. every time we shift a pointer, we are essentially ruling out any other solutions that involve that pointer because it will ALWAYS bottleneck.
        """

        res = 0
        L, R = 0, len(heights) - 1

        while L < R:
            res = max(res, (R - L) * min(heights[L], heights[R]))

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return res