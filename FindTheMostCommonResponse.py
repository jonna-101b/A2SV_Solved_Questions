from collections import defaultdict
from typing import List

class Solution:
    def findCommon(self, occurrence: defaultdict[str: int], max_response: int) -> str:
        commons = []

        for response in occurrence:
            if occurrence[response] == max_response:
                commons.append(response)

        if len(commons) == 1: return commons[0]
        
        commons.sort()
        return commons[0]

    def findCommonResponse(self, responses: List[List[str]]) -> str:
        occurrence = defaultdict(int)
        max_response = 0

        for day in responses:
            found = set()
            for response in day:
                if response not in found:
                    occurrence[response] += 1
                    found.add(response)
                    max_response = max(max_response, occurrence[response])

        return self.findCommon(occurrence, max_response)
