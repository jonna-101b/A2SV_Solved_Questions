n,m = map(int, input().split())
nums=list(map(int, input().split()))
total=0
ans=0
left=0
for right in range(n):
    total+=nums[right]
    while total>m:
        total-=nums[left]
        ans+=n-right
        left+=1


print(ans)
