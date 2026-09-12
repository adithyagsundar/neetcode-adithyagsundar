class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        if the sum of the two pointers is too large, then the rightmost number CAN NOT be included becasue its being added to the smallest remaining number yet its still too big, so we decrement
        same logic for if the sum is too small, this time we increment
        """
        L, R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] < target: 
                L += 1 # leftmost number is too small, will not be included
            if numbers[L] + numbers[R] > target:
                R -= 1 #rightmost number is too big, will not be included
            if numbers[L] + numbers[R] == target:
                return [L + 1, R + 1] #1-indexed
        