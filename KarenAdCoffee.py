n, k, q = map(int, input().split())
maxi = 200000 + 3

endpoints = [0] * maxi
for _ in range(n):
    l, r = map(int, input().split())
    endpoints[l] += 1
    if r + 1 < maxi:
        endpoints[r + 1] -= 1

prefix = [0] * maxi
prefix[0] = endpoints[0]
for i in range(1, maxi):
    prefix[i] = prefix[i - 1] + endpoints[i]

valid = [0] * maxi
for i in range(maxi):
    if prefix[i] >= k:
        valid[i] = 1

pref_valid = [0] * maxi
pref_valid[0] = valid[0]
for i in range(1, maxi):
    pref_valid[i] = pref_valid[i - 1] + valid[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(pref_valid[r] - pref_valid[l - 1])
