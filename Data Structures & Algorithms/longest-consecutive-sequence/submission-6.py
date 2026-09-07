class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        check if the number before the current number is in the set to identify the start of a sequence
        if it is the start of a sequence, keep increasing by one until that value is not in the sequence
        add this to the current length
        take max length of current lenghts
        """

        numSet = set(nums) #set to remove duplicates and to search up numbers in O(1)

        longest = 0

        for num in nums:
            if num - 1 not in numSet: #start of a sequence, searching through set is constant time
                length = 0
                while num + length in numSet: #since length = 0, we start ON the first number itself (num + 0)
                    length += 1
                longest = max(length, longest)
        return longest
            
                

