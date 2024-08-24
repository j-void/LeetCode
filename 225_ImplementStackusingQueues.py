class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        output = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return output

    def top(self) -> int:
        output = 0
        while self.queue1:
            output = self.queue1.popleft()
            self.queue2.append(output)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return output
        

    def empty(self) -> bool:
        if self.queue1:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
