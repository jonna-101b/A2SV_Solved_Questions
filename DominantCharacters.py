def solve(s: str, n: int) -> int:
    for i in range(1, n):
        occurrence = { "a": 0, "b": 0, "c": 0 }
        counter = 0

        while counter < i:
            occurrence[s[counter]] += 1
            counter += 1

        last = 0
        for j in range(counter, n):
            occurrence[s[j]] += 1

            if occurrence["a"] > occurrence["b"] and occurrence["a"] > occurrence["c"]:
                return i+1

            occurrence[s[last]] -= 1
            last += 1

    return -1
    

if __name__ == "__main__":
    no_of_testcases = int(input())
    for _ in range(no_of_testcases):
        n = int(input())
        s = input().strip()
        print(solve(s, n))