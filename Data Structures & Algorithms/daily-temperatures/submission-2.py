class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        create a stack that holds the pair of the temperature and the its index
        this stack holds the temperatures that have NOT been popped yet (i.e. there has not been a larger value yet)
        when a larger value is found, add to result at the index of the ELEMENT WE ARE POPPING the difference between the current element and the element we are popping
        add current element to the stack        
        """

        res = [0] * len(temperatures) # don't need to fill in zeroes for nonvalues since we already do here

        stack = [] # [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # while loop because one value added can be larger than multiple current values in the stack
                stackT, stackInd = stack.pop() # using the list we had in res, we are storing the ORIGINAL INDEX of the value here from temperatures, which goes into the same index in res
                res[stackInd] = (i - stackInd) # currnet index - original index
            stack.append([t, i])
        return res

        