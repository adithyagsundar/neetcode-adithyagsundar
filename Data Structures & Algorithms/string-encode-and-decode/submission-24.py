class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        5#string
        """

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        two pointers, i and j
        i is at the start of the string and j goes through the string
        use the length of the string (first charcter) to know how far to append to the result list
        """
        
        res = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[j - 1])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res





