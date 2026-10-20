class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        create a hashmap that stores the values in nums and their indices
        difference = target - nums[i]
        the ONLY value that can add to nums[i] to make target is difference
        therefore, if difference is in the hashmap (also in the array) then it is a two sum and we return those indices
        iterate through each value of nums and check if the difference of target and that value is in the hashmap, if it is return the indices
        """ 

        indices = {}

        for i, num, in enumerate(nums):
            indices[num] = i #num, index

        for i, num in enumerate(nums):
            diff = target - num #diff must exist in the hashmap to be a two sum
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []

        