class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        create a hashmap with the number and the index of it
        if the difference of the current number with the target is in the hashmap, then return those indices
        """

        indices = {}

        for i, num in enumerate(nums):
            indices[num] = i

        for i, num in enumerate(nums):
            diff = target - num

            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return 0
      
    
        