class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        for each number, do two sum II
        to avoid duplicates, first skip any consecutive i values
        then when we find a match, skip any consecutive L values 
        """

        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: # if you skip consecutive i values, duplicates are skipped
                continue
            L, R = i + 1, len(nums) - 1

            while L < R:
                threeSum = num + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                if threeSum < 0:
                    L += 1
                if threeSum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1 # must move because there can be multiple pairs for one i value
                    while L < R and nums[L] == nums[L - 1]: # if you skip consecutive L values, dupplicates are skipped
                        L += 1
        return res
