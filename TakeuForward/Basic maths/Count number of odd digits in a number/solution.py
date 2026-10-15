n=int(input())
cnt=0
while n>0:
    num=n%10
    if num % 2 ==1:
        cnt+=1
    n//=10
print(cnt)

