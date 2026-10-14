n=int(input())
for i in range(1,n*2):
    if i >n:
        i=(2*n)-i
    for j in range(i):
        print("*",end=' ')
    for j in range((n-i)*2):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()