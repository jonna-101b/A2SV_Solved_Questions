def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    ans = None
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            ans = arr[mid]
            r = mid - 1
        else:
            l = mid + 1
    return ans


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    
    prev = -10**18   
    can = True
    
    for i in range(n):
     
        option1 = a[i] if a[i] >= prev else float('inf')

        target = prev + a[i]
        bj = binary_search(b, target)
        
        if bj is not None:
            option2 = bj - a[i]
        else:
            option2 = float('inf')
        
        best = min(option1, option2)
        
        if best == float('inf'):
            can = False
            break
        
        prev = best  
    
    if can:
        print("YES")
    else:
        print("NO")
