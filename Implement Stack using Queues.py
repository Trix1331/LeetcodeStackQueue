class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if self.queue1 is []:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
            while self.queue1:
                self.queue2.append(self.queue1.pop(0))
            self.queue1, self.queue2 = self.queue2, self.queue1
    def pop(self) -> int:
        return self.queue1.pop(0)

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1
