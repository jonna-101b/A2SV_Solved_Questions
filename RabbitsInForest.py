from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        rabbits = 0
        for i in count:
            max_rabbits = i + 1
            groups = math.ceil(count[i] / max_rabbits)
            rabbits += groups * max_rabbits
        return rabbits
