class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        last_num = None

        for num in nums:
            if last_num is not None and num == last_num:
                return True

            last_num = num

        return False
