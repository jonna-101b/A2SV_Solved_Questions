if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, l, r = [ int(num) for num in input().strip().split() ]
        socks = [ int(num) for num in input().strip().split() ]
        left = set(socks[:n//2])
        right = set(socks[n//2:])
        costs = abs(n//2 - l) + len(left - right)
        print(costs)