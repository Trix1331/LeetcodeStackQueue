class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack.pop(0)

    def peek(self) -> int:
        '''
        Get the front element.
        :rtype: int
        '''
        if not self.stack:
            return None
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0

obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()