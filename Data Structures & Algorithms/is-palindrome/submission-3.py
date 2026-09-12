class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_reverse = reversed(s)

        if s_reverse.lower() == s.lower():
            return True
        else:
            return False
