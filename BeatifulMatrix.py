row = None
col = None

for i in range(5):
    val = list(map(int, input().split()))
    found = False
    if not found:
        for j in range(5):
            if val[j] != 0:
                found = True
                row = i
                col = j
print(abs(2 - row) + abs(2 - col))
