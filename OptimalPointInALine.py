if __name__ == "__main__":
    n = int(input())
    points = [int(num) for num in input().strip().split()]
    points.sort()
    median = (n - 1)//2 if n % 2 == 0 else n//2
    print(points[median])