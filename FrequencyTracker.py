from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.occurrence = defaultdict(int)
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None:
        if self.occurrence[number] and self.frequency[self.occurrence[number]]:
            self.frequency[self.occurrence[number]] -= 1

        self.occurrence[number] += 1
        self.frequency[self.occurrence[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.occurrence[number]:
            self.frequency[self.occurrence[number]] -= 1
            self.occurrence[number] -= 1

            if self.occurrence[number]:
                self.frequency[self.occurrence[number]] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency[frequency] > 0