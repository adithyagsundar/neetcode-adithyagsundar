class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        L and R pointers are the same, if non alphanumeric then skip
        """

        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not self.isAlphaNum(s[L]):
                L += 1
            while L < R and not self.isAlphaNum(s[R]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True

    def isAlphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'))
    

