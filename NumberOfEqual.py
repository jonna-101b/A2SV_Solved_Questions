from collections import Counter
n,m = map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

count=Counter(a)
count2=Counter(b)
ans=0

for key,val in count.items():
    if key in count2:
        ans+=val*count2[key]
print(ans)
