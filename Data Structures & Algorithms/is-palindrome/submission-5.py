class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        s.replace(" ", "")

        while L < R:
            while L < R and not self.alphaNum(s[L]):
                L += 1
            while L < R and not self.alphaNum(s[r]):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True
