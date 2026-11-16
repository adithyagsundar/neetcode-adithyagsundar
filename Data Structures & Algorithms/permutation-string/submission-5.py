class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        use two hashmaps to store the frequency of each character, a-z
        to avoid checking each hashmap every iteration (O(26 * n)), create a matches variable that holds the current number of matches between the hashmaps
        """
        count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        window = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        L = 0

        for c in s1:
            count[c] = 1 + count.get(c, 0)

        matches = sum(count[c] == window[c] for c in count)

        # check every window with size of s1
        for R in range(len(s2)):
            window[s2[R]] = 1 + window.get(s2[R], 0) # adding each character to the window

            if window[s2[R]] == count[s2[R]]:
                matches += 1

            if (R - L + 1 > len(s1)): # keep window size equal to len(s1)
                window[s2[L]] = window[s2[L]] - 1 # remove from window
                if window[s2[L]] == count[s2[L]]:
                    matches -= 1
                L += 1 
            
            if matches == 26:
                return True
        return False
        







                