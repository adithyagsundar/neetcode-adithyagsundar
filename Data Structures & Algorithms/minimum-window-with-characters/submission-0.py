class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        window = {}
        L = 0
        res = ""


        for c in t:
            count[c] = 1 + count.get(c, 0)

        for R in range(len(s)):
            if s[R] in count:
                window[s[R]] = 1 + window.get(s[R], 0)
                res += window[s[R]]
            else:
                L += 1
        return res
            

        