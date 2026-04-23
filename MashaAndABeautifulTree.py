from typing import Optional, List
from math import log2

def solve(n: int, p: List[int]) -> int:
    index = -1
    ops = 0

    def DFS(counter: int = 0) -> Optional[List[int]]:
        nonlocal index, ops

        if ops == -1:
            return None

        if counter == n:
            index += 1
            return [p[index], p[index]]
        
        r1 = DFS(counter + 1)
        r2 = DFS(counter + 1)

        if r1 is None or r2 is None:
            return None
        
        if r1[1] < r2[0]:
            return [r1[0], r2[1]]
        elif r2[1] < r1[0]:
            ops += 1
            return [r2[0], r1[1]]
        else:
            ops = -1
            return None
        
    res = DFS()
    return -1 if res is None else ops


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(log2(int(input())))
        p = list(map(int, input().split()))
        print(solve(n, p))