from collections import deque

class DataStream:

    def __init__(self, value: int, k: int):
        self.window = deque(maxlen = k)
        self.target = value
        self.max = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.count += 1 if num != self.target else 0
        if len(self.window) == self.max and self.window[0] != self.target:
            self.count -= 1
            
        self.window.append(num)
        return self.count == 0 and len(self.window) == self.max
