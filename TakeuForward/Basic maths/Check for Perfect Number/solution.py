n=int(input())
sum_=0
for i in range(1,n):
    if n%i == 0:
        sum_+=i
print(sum_==n)
