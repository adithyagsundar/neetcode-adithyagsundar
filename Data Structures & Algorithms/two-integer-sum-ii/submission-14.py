class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            num1 = target - nums[i]
            l = 0
            h = i-1
            # print()
            # print(nums[i])
            # print("num1: ", num1)
            while l <= h:
                mid = (l + h) // 2
                if nums[mid] == num1:
                    return [mid+1, i+1]
                elif nums[mid] < num1:
                    l = mid+1
                else:
                    h = mid-1
        
        return [-1, -1]