class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        self.instack.append(x)

    def pop(self) -> int:
        peek = self.peek()
        self.outstack.pop()
        return peek

    def peek(self) -> int:
        if self.outstack:
            return self.outstack[-1]
        if not self.instack:
            return -1
        while self.instack:
            self.outstack.append(self.instack.pop())
        return self.outstack[-1]

    def empty(self) -> bool:
        if not self.instack and not self.outstack:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()