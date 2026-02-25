from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        skill_sum = skill[left] + skill[right]
        chemistry = 0

        while left < right:
            if skill[left] + skill[right] == skill_sum:
                chemistry += skill[left] * skill[right]
                left += 1
                right -= 1

            else:
                return -1

        return chemistry
