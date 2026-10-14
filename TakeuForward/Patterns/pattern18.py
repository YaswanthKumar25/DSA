n=int(input())
for i in range(1,n+1):
    pattern=65+n-i
    for j in range(i):
        print(chr(pattern),end=' ')
        pattern+=1
    print()