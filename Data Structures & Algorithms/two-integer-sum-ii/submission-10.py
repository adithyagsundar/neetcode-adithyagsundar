class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        two pointers, if less than target then move the left pointer. if greater than target then move the right pointer.
        """

        L , R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] > target:
                L += 1
            if numbers[L] + numbers[R] < target:
                R -= 1
            if numbers[L] + numbers[R] == target:
                return [L, R]
        return [0, 0]        