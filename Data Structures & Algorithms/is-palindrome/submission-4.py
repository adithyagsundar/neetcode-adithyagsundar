class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_reverse = str(reversed(s))

        if s_reverse.lower() == s.lower():
            return True
        else:
            return False
