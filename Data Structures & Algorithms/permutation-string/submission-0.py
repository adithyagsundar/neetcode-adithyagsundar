class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count = {0} * 26
        window = {0} * 26
        L = 0
        matches = 0 # if this becomes 26, we stop the algorithim

        for c in s1:
            count[c] = 1 + count.get(c, 0)

        # check every window with size of s1
        for R in range(len(s2)):
            window[s2[R]] = 1 + window.get(s2[R], 0) # adding each character to the window

            if (R - L + 1 > len(s1)): # keep window size equal to len(s1)
                window[s2[L]] = window[s2[L]] - 1 # remove from window
                L += 1 
            
            if window == count:
                return True
        return false





                