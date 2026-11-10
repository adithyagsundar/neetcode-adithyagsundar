class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        res = 0

        for R in range(len(s)):
            if s[R] in seen:
                # if there is a duplicate
                res = max(res, len(seen))
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
        return res 
        