class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        two pointers, one on the left and right
        if every character at each pointer is the same while they increment/decrement, until the pointers meet, then it is a valid palindrome
        we only want to consider alphanumeric characaters, so we create a new function using ASCII values (since all ASCII values for A to Z or a to z or 0 to 9 are contiguous)
        """
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not self.isAlphaNum(s[L]): # include L < R because the loop might run out of bounds before checking the outer loop
                L += 1
            while R > L and not self.isAlphaNum(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True

    def isAlphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
               ord("a") <= ord(c) <= ord("z") or
               ord("0") <= ord(c) <= ord("9"))
    

