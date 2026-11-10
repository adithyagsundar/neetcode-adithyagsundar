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
            seen.add(s[R]) 
            res = max(res, len(seen)) # compute the max only after adding the most recent. we already computed the max length FROM THE PREVIOUS ITERATION when we encounter a duplicate.
        return res 
        