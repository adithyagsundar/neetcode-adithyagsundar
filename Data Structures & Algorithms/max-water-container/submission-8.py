class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        two pointers, if the height of a rectangle is less, then shift that pointer
        this works because we are guaranteed to find the highest rectangle here and check it against everything
        store max area into res and return
        """

        res = 0
        L, R = 0, len(heights) - 1

        while L < R:
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
                res = max(res, min(heights[L], heights[R]) * (R - L))
        return res
                