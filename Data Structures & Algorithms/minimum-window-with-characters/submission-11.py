class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        window = {}
        L = 0
        res = ""


        for c in t:
            count[c] = 1 + count.get(c, 0)

        have, need = 0, len(count)

        for R in range(len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)
            if s[R] in count and window[s[R]] == count[s[R]]:
                have += 1
            
            while have == need:
                res += s[R]
                window[s[L]] -= 1
                L += 1
                have -= 1
        return res
            

        