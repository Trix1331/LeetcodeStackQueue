class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self._move_stack1_to_stack2()
        return self.stack2.pop()

    def peek(self) -> int:
        '''
        Get the front element.
        :rtype: int
        '''
        self._move_stack1_to_stack2()
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2

    def _move_stack1_to_stack2(self):
        '''
        Moves all elements from stack1 to stack2 if stack2 is empty.
        This ensures that the oldest elements are at the top of stack2,
        simulating the behavior of a queue.
        '''
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()