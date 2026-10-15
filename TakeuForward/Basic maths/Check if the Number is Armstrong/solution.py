n=int(input())
dup=n
sum_=0
while n>0:
    num=n%10
    sum_+=num**len(str(dup))
    n//=10
print(dup==sum_)
