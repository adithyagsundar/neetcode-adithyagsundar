class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        for each number, do two sum II
        to avoid duplicates, 
        """

        nums.sort()
        res = []

        for i, num in enumerate(nums):
            L, R = i + 1, len(nums) - 1

            while L < R:
                threeSum = num + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                if threeSum < 0:
                    L += 1
                if threeSum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while nums[L] == nums[L - 1]:
                        L += 1
        return res
