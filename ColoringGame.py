import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # a is given in non-decreasing order

    ans = 0
    M = a[n - 1]

    for k in range(2, n):
        # threshold: a[i]+a[j] must strictly exceed this
        if k == n - 1:
            threshold = a[k]          # only condition A matters (B always satisfied)
        else:
            threshold = max(a[k], M - a[k])  # conditions A and B merged

        # count pairs (i,j) with i<j<k and a[i]+a[j] > threshold (two pointers)
        l, r = 0, k - 1
        while l < r:
            if a[l] + a[r] > threshold:
                ans += r - l   # a[l] paired with a[l+1..r] all satisfy it
                r -= 1
            else:
                l += 1

    print(ans)
