class MinStack:

    def __init__(self):

        self.stack = []
        self.minStack = []

    def push(self, val):

        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)

        else:
            currentMinimum = min(val, self.minStack[-1])
            self.minStack.append(currentMinimum)

    def pop(self):

        self.stack.pop()
        self.minStack.pop()

    def top(self):

        return self.stack[-1]

    def getMin(self):

        return self.minStack[-1]
        
minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())