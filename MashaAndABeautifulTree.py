from typing import Optional, List
from math import log2

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n = int(log2(int(input())))
        p = list(map(int, input().split()))
        index = -1
        ops = 0

        def DFS(counter: int = 0) -> Optional[List[int]]:
            global n, p, index, ops

            if counter == n:
                index += 1
                return [p[index], p[index]]
            
            r1 = DFS(counter + 1)
            r2 = DFS(counter + 1)
            if r1 is None or r2 is None:
                return None
            
            if r1[0] < r2[0] and r1[1] < r2[0]:
                return [r1[0], r2[1]]
            elif r1[0] > r2[0] and r1[0] > r2[1]:
                ops += 1
                return [r2[0], r1[1]]
            else:
                ops = -1
                return None
            
        DFS()
        print(ops)