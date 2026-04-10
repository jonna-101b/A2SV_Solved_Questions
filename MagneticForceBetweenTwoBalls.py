class Solution:
    def __init__(self):
        self.position = []

    def can_place(self, m, dist):
        count = 1  # first ball placed at first self.position
        last = self.position[0]

        for i in range(1, len(self.position)):
            if self.position[i] - last >= dist:
                count += 1
                last = self.position[i]
            
            if count >= m:
                return True

        return False
    
    def maxDistance(self, position: List[int], m: int) -> int:
        self.position = sorted(position)
        left = 1
        right = self.position[-1] - self.position[0]
        result = 0

        while left <= right:
            mid = (left + right) // 2

            if self.can_place(m, mid):
                result = mid
                left = mid + 1  # try bigger distance
            else:
                right = mid - 1  # try smaller distance

        return result
