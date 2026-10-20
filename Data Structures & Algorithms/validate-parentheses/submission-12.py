class Solution:
    def isValid(self, s: str) -> bool:
        """
        ][
        )]}{[(
        every opening bracket comes BEFORE a closing bracket
        use a hashmap to map closing to opening brackets
        if a closing bracket, check if the correspondign open bracket is at the TOP OF THE STACK. this is because we want to make sure that there are NO OTHER brackets in between
        """
        stack = []
        pairs = {"]": "[", "}" : "{", ")" : "("}

        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]: # if stack is NOT empty (i.e. there are opening brackets) and the last element of the stack is the corresponding opening bracket
                    stack.pop() # then we can remove from the stack
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0