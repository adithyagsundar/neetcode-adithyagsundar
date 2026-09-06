class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        create a boundary for each height based on how much it can "extend"
        therfore, the stack of heights will be in increasing order, because then everything can extend. if there's a decreasing value after, then the one before can no longer extend because theres a hole
        when we get a decreasing value, pop the previous value and compute the max area of it using the left and right bounds
        
        """
