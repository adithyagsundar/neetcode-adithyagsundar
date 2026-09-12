class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] < target: 
                L += 1 # leftmost number is too small, will not be included
            if numbers[L] + numbers[R] > target:
                R -= 1 #rightmost number is too big, will not be included
            if numbers[L] + numbers[R] == target:
                return [L, R]
        