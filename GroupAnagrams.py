from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = dict()
        repeated_words = defaultdict(int)

        for word in strs:
            if word in sorted_dict:
                repeated_words[word] += 1
                continue

            sorted_dict[word] = "".join(sorted(word))

        frequency_dict = dict()
        for word in sorted_dict:
            if sorted_dict[word] in frequency_dict:
                frequency_dict[sorted_dict[word]] += [word]
            
            else:
                frequency_dict[sorted_dict[word]] = [word]

            if word in repeated_words:
                frequency_dict[sorted_dict[word]] += [word]*repeated_words[word]

        res = []
        for words in frequency_dict.values():
            res.append(words)

        return res