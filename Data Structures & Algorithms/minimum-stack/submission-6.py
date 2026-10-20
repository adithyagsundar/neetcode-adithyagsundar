class MinStack:

    """
    the only hard part about this problem is getting the min value in O(1) time
    to do this, we create another stack, minStack, where the top value of minStack is always the minimum value of all the values so far
    that way, when we pop a value, we are still able to find the min value just by ALWAYS looking at the TOP value of the minStack
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) #minimum of the new value and the value on the top of the stack, this is what will be pushed
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() #we need to pop from both of the stacks, since the min value is at the corresponding index

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
