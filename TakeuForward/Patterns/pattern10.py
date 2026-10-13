n=int(input())
for i in range(1,n*2):
    if i<=n:
        i=i
    else:
        i=n-1
        n=n-1
    for j in range(i):
        print("*",end=" ")
    print()