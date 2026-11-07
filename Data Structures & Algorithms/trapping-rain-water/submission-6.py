class Solution:
    def trap(self, height: List[int]) -> int:
        """
        O(n) space
        for each position, there is a left boundary and right boundary
        the bottleneck if the MINIMUM of those boundaries
        then, we need to subtract the area of the position we are lookign at itself. if its greater than the minimum height, then we obviously can't store any water there.
        minLR is the MAXIMUM amount of water taht can fit in a given column
        minLR[i] - height[i] = area
        """



        """
        O(1) space:
        when you shift the left pointer, you KNOW that the left side has to be the bottle neck becasue it was less than the right side, regardless of what the NEW value is
        same for right pointer as well
        calculate the water at the latest pointer you jsut shifted
        """

        """
        O(n) space
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
        """


        L, R = 0, len(height) - 1
        res = 0
        leftMax, rightMax = height[L], height[R]

        while L < R:
            if leftMax < rightMax:
                L += 1
                res += max(0, leftMax - height[i])# we KNOW that left is the BOTTLENECK, since we just moved it
                leftMax = max(leftMax, height[i])
            else:
                R -= 1
                res += max(0, rightMax - height[i])
                rightMax = max(rightMax, height[i])
        return res
            


            