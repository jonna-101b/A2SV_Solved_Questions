import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().strip() for _ in range(n)]

    g = [[] for _ in range(26)]
    indeg = [0] * 26
    used = [False] * 26

    for w in words:
        for c in w:
            used[ord(c) - 97] = True

    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        found = False

        for j in range(min_len):
            if w1[j] != w2[j]:
                u = ord(w1[j]) - 97
                v = ord(w2[j]) - 97
                g[u].append(v)
                indeg[v] += 1
                found = True
                break

        if not found and len(w1) > len(w2):
            print("Impossible")
            return

    q = deque()
    for i in range(26):
        if indeg[i] == 0:
            q.append(i)

    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if len(order) != 26:
        print("Impossible")
        return

    res = ''.join(chr(i + 97) for i in order)
    print(res)

if __name__ == "__main__":
    solve()
