def prime(num):
    cnt=0
    for i in range(1,num+1):
        if num%i==0:
            cnt+=1
    return True if cnt == 2 else False

n=int(input())
cnt=0
for i in range(1,n+1):
    num=prime(i)
    if num:
        cnt+=1
print(cnt)




