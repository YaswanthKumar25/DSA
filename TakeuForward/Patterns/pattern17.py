n=int(input())
for i in range(1,n+1):
    pattern=65
    for j in range(n-i):
        print(" ",end=' ')
    for j in range(i):
        print(chr(pattern),end=' ')
        pattern+=1
    pattern-=1
    for j in range(i-1,0,-1):
        pattern-=1
        print(chr(pattern),end=' ')
    print()
