class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        if the length of the window - the frequency of the most frequent character in the window <= k, then it is a valid window
        beacause there is enough OTHER characters for us to replace
        keep a hashmap to store the frequencies of each value
        """

        res = 0
        L = 0
        count = {} # to find the most frequent character

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            if (R - L + 1) - max(count.values()) <= k:
                res = max(res, R - L + 1)
            else:
                L += 1
                count[s[R]] -= 1
            res = max(res, R - L + 1)
        return res