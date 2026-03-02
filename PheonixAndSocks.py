from collections import Counter

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, l, r = [ int(num) for num in input().strip().split() ]
        socks = [ int(num) for num in input().strip().split() ]
        left = socks[:n//2]
        right = Counter(socks[n//2:])
        costs = abs(n//2 - l)

        for num in left:
            if num not in right or right[num] == 0:
                costs += 1
                continue

            right[num] -= 1
            
        print(costs)