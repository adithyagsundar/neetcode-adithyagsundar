class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res # 3#dog3#cat5#mouse5#horse


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): #do not use for loop because we iterate i based on the value of j
            j = i #start where i is each time
            while s[j] != "#":
                j += 1 #iterate j until number is passed
            length = int(s[i: j]) #for if number is double digit
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res



