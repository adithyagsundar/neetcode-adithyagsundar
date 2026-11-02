class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        for each number, do two sum for all other numbers
        since there can not be duplicates, skip starting numbers that are the SAME as the previous number
        if you have the same starting number for two lists, the chance that there is a duplicate is VERY HIGH
        to find EVERY pair, update the left pointer only to move to the next set of values, skip it if it is the same as the previous value
        """

        res = []
        nums.sort()

        for i, v in enumerate(nums):
            #skip any duplicate starting values
            if v == nums[i - 1]: 
                continue

            #two sum for each number
            L, R = 0, len(nums) - 1
            while L < R:
                threeSum = v + nums[L] + nums[R] # new threeSum for every index
                if threeSum > 0:
                    R -= 1
                if threeSum < 0:
                    L += 1
                if threeSum == 0:
                    res.append([v, nums[L], nums[R]])

                L += 1
                while nums[L] == nums[L - 1] and L < R:
                    L += 1
        return res
