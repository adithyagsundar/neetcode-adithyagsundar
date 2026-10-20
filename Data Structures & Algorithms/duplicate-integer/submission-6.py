class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        create seen hashset
        iterate through nums, if current num is not already in the hashset then add it
        if it is, then return true
        adding values and searching values in a hashet is O(1)
        so total time complexity is O(n) since we iterate through the list once
        but its not O(nlogn) since we dont search through a regular array
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

