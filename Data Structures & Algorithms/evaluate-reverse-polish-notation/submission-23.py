class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        create a stack that holds the result of the last operation
        add the newest number to the stack, then perform the operation
        """

        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(token))
        return stack[-1]