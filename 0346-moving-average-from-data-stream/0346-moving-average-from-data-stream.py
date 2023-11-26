from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.q = deque([])
        self.size = size 
        self.tot = 0
    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            l = self.q.popleft()
            self.tot -= l 
        self.q.append(val)
        self.tot += val 
        return self.tot / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)