class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.minimum and val <= self.minimum[-1]:
            self.minimum.append(val)
        elif not self.minimum:
            self.minimum.append(val)
    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.minimum[-1]:
            self.minimum.pop()
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
