n=int(input())
maxi=float('-inf')
while n>0:
    num=n%10
    maxi=max(maxi,num)
    n//=10
print(maxi)