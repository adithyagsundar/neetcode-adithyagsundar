class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        create a boundary for each height based on how much it can extend
        therefore, the stack of heights will be in increasing order, because then everything can extend. if there's a decreasing value after, then the one before can no longer extend because theres a hole
        when we get a decreasing value, pop the previous value and compute the max area of it using the left and right bounds
        we then need to extend the width of the value we are adding to the left
        heights left in the stack go all the way to the end of the histogram
        """

        maxArea = 0

        stack = [] # [index, height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h: # last height greater, so we pop the last height and compute maxArea
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index # extending to the left
            stack.append([start, h]) # start = i so it works for regular ones
        for i, h in stack:
            maxArea = max(maxArea, h * (len(stack) - i))
        return maxArea
