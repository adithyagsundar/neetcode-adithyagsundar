class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        if two strings have the same frequency map, then they are anagrams
        create a hashmap, and put all strings with the same freq map in that value
        freq_map : [str1, str2, str3, etc.]
        print values of hashmap in list 
        """

        res = defaultdict(list) #for if the count doesn't already exist

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 #take count of every character, a @ 0, b @ 1, c # 2, etc.
            res[tuple(count)].append(s) 
        
        return list(res.values())

        



                



