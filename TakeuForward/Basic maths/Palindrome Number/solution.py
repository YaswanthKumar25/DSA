n=int(input())
dup=n
num=0
while n>0:
    num=(num*10)+(n%10)
    n//=10
print(dup==num)