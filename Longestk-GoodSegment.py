import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

freq = defaultdict(int)
left = 0
distinct = 0

l = 0
r = 0
max_len = 0

for right in range(n):
    if freq[a[right]] == 0:
        distinct += 1
    freq[a[right]] += 1

    while distinct > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            distinct -= 1
        left += 1

    if right - left + 1 > max_len:
        max_len = right - left + 1
        l = left
        r = right

print(l + 1, r + 1)
