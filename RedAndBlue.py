t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    b=list(map(int,input().split()))


    max_a,tot=0,0
    for ai in a:
        tot+=ai
        max_a=max(max_a,tot)

    max_b,tot=0,0
    for bi in b:
        tot+=bi
        max_b=max(max_b,tot)

    print(max_a+max_b)
