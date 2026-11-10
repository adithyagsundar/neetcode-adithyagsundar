class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        res = 0

        for R in range(len(s)):
            while s[R] in seen: # could be multiple of the same duplicate
                # if there is a duplicate
                seen.remove(s[L])
                L += 1
            res = max(res, len(seen))
            seen.add(s[R])
        return res 
        