class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        5#string
        """

        res = ""

        for s in strs:
            res += string(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        two pointers, i and j
        i is at the start of the string and j goes through the string
        use the length of the string (first charcter) to know how far to append to the result list
        """
        
        res = []

        i = 0

        for c in s:
            j = i
            while j != "#":
                j += 1
            length = int(s[i])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res





