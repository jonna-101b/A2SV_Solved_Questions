import heapq

n = int(input())

heap = []
result = []

for _ in range(n):
    command = input().split()

    if command[0] == "insert":
        x = int(command[1])
        heapq.heappush(heap, x)
        result.append(f"insert {x}")

    elif command[0] == "removeMin":
        if not heap:
            result.append("insert 0")
            heapq.heappush(heap, 0)

        heapq.heappop(heap)
        result.append("removeMin")

    else:  # getMin x
        x = int(command[1])

        # Remove all smaller elements
        while heap and heap[0] < x:
            heapq.heappop(heap)
            result.append("removeMin")

        # If x is not present as minimum, insert it
        if not heap or heap[0] != x:
            heapq.heappush(heap, x)
            result.append(f"insert {x}")

        result.append(f"getMin {x}")

print(len(result))
print("\n".join(result))
