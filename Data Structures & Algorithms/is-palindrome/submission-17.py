class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        L and R pointers are the same, if non alphanumeric then skip
        """

        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not s[L].isAlphaNum:
                L += 1
            while L < R and not s[R].isAlphaNum:
                R -= 1
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True

    def isAlphaNum(self, c):
        return (ord('a') <= c <= ord('z') or ord('A') <= c <= ord('Z') or ord('1') <= ord(c) <= ord('9'))
    

