#binary value of a number
n=int(input("enter a number:"))
binary=''
while n>0:
    binary=str(n%2)+binary
    n=n//2
print("binary value of the number is:", binary)


