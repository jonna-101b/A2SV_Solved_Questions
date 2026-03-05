n,m = map(int, input().split())
nums=list(map(int, input().split()))
total,left=0,0
ans=0
for right in range(n):
    total+=nums[right]
    while total>m:
        total-=nums[left]
        left+=1

    ans+=right-left+1
print(ans)
