class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []   # store the minimums at each point in case we pop

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            self.min.append(min(val, self.min[-1]))
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # get O(1) time at expense of O(n) ram space
        return self.min[-1]
