if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        n, coins = [ int(num) for num in input().strip().split() ]
        casinos = []
        
        for __ in range(n):
            l, r, real = [ int(num) for num in input().strip().split() ]
            casinos.append((l, r, real))

        casinos.sort(key = lambda x: x[0])
        
        for l, r, real in casinos:
            if l <= coins <= r:
                coins = max(coins, real)

        print(coins)
