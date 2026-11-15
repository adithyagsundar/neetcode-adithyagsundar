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
        maxf = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxf = max(maxf, count[s[R]])
            if (R - L + 1) - maxf <= k:
                res = max(res, R - L + 1)
            else:
                count[s[L]] -= 1
                L += 1
        return res