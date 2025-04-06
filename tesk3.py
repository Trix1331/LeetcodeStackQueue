from collections import deque

class FreqStack:
    """
    Реалізація структури даних, що підтримує операції push, pop та maxFreq.
    - push(val): додає значення val у стек.
    - pop(): видаляє та повертає значення з найбільшою частотою.
    - maxFreq(): повертає найбільшу частоту елементів у стеці.
    """

    def __init__(self):
        '''
        Ініціалізація структури даних.
        '''
        self.freq = {}
        self.group = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        '''
        Додає значення val у стек.
        '''
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        f = self.freq[val]
        if f > self.maxFreq:
            self.maxFreq = f
        if f not in self.group:
            self.group[f] = deque()
        self.group[f].append(val)

    def pop(self) -> int:
        x = self.group[self.maxFreq].pop()
        self.freq[x] -= 1
        if len(self.group[self.maxFreq]) == 0:
            del self.group[self.maxFreq]
            self.maxFreq -= 1

        return x


fs = FreqStack()
fs.push(5)
print("Після push(5)")

fs.push(7)
print("Після push(7)")

fs.push(5)
print("Після push(5)")

fs.push(7)
print("Після push(7)")

fs.push(4)
print("Після push(4)")

fs.push(5)
print("Після push(5)")

print("pop():", fs.pop())  # Очікується 5
print("pop():", fs.pop())  # Очікується 7
print("pop():", fs.pop())  # Очікується 5
print("pop():", fs.pop())  # Очікується 4
