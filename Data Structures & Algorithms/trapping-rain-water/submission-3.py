class Solution:
    def trap(self, height: List[int]) -> int:
        """
        for each position, there is a left boundary and right boundary
        the bottleneck if the MINIMUM of those boundaries
        then, we need to subtract the area of the position we are lookign at itself. if its greater than the minimum height, then we obviously can't store any water there.
        """
        res = 0

        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minLR = [0] * len(height)


        valMax = 0

        for i in range(len(height)):
            maxLeft[i] = valMax
            valMax = max(valMax, height[i])

        valMax = 0

        for i in range(len(height) -1, -1, -1):
            maxRight[i] = valMax
            valMax = max(valMax, height[i])

        for i in range(len(maxLeft)):
            minLR[i] = min(maxLeft[i], maxRight[i])

        for i in range(len(height)):
            res += max(0, minLR[i] - height[i])

        return res
            