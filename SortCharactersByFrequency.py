from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        occurrence = Counter(s)
        occurred = [(char, occurrence[char]) for char in occurrence]
        occurred.sort(key = lambda x: x[1], reverse = True)
        arranged = []

        for char, frequency in occurred:
            arranged += [char]*frequency

        return "".join(arranged)
