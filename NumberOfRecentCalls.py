from collections import deque

class RecentCounter:

    def __init__(self):
        self.pings = deque()
        self.end = 3000

    def ping(self, t: int) -> int:
        self.pings.append(t)
        self.end = t if t > self.end else self.end

        while self.pings[0] < self.end - 3000:
            self.pings.popleft()

        return len(self.pings)
