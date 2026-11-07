class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        L, R = 0, len(heights) - 1

        while L < R:
            max(res, (R - L) * min(heights[L], heights[R]))

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return res
