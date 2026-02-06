from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        check = { list1[i]: i for i in range(len(list1)) }
        res = []
        order = None

        for i in range(len(list2)):
            if list2[i] in check:
                curr_order = i + check[list2[i]]
                if order is None or curr_order <= order:
                    if order is not None and curr_order < order:
                        res = []

                    res.append(list2[i])
                    order = curr_order

        return res