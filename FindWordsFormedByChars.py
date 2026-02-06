from typing import List

class Solution:
    def countGoodWordsLength(self, words: List[str]) -> int:
        counter = 0
        for word in words:
            counter += len(word)

        return counter 

    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = dict()
        for char in chars:
            if char in chars_dict:
                chars_dict[char] += 1
                continue
            
            chars_dict[char] = 1


        good = []
        for word in words:
            all_seen = True
            chars_copy = chars_dict.copy()

            for char in word:
                if char in chars_copy and chars_copy[char]:
                    chars_copy[char] -= 1
                    continue

                all_seen = False
                break
            
            if all_seen:
                good.append(word)

        return self.countGoodWordsLength(good)