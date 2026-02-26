class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orders = {order[i]: i for i in range(len(order))}
        last = len(order)

        for i in range(ord('a'), ord('z') + 1):
            char = chr(i)
            if char not in orders:
                orders[char] = last
                last += 1

        return "".join(sorted(s, key = lambda x: orders[x]))