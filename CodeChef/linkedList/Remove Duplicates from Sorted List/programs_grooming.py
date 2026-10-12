# #binary value of a number
# n=int(input("enter a number:"))
# binary=''
# while n>0:
#     binary=str(n%2)+binary
#     n=n//2
# print("binary value of the number is:", binary)

# #binary to decimal value of a number
# binary=input("enter a binary number:")
# decimal=0
# for digit in binary:
#     decimal=decimal*2+int(digit)
# print("decimal value of the number is:", decimal)

# #write a program to sort the list without using sort method
# #selection sort
# a=[5, 2, 9, 1, 5, 6]
# for i in range(len(a)):
#     mini=i
#     for j in range(i,len(a)):
#         if a[j]<a[mini]:
#             mini=j
#     a[i],a[mini]=a[mini],a[i]
# print(a)

# a=['f','s','r','a','b']
# n=len(a)
# for i in range(n):
#     for j in range(n-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# #write a program to sort dic by key
# d={'a':10 , 'b':8,'c':5,'d':3}
# li=list(d.items())
# for i in range(len(li)):
#     for j in range(len(li)-i-1):
#         if li[j][1]>li[j+1][1]:
#             li[j],li[j+1]=li[j+1],li[i]
# dic={}
# for k,v in li:
#     dic[k]=v
# print(dic)

#write a program to find max value key
# dic={'a':10,'b':5,'c':8,'d':3}
# maxi=float('-inf')
# char=''
# for key,val in dic.items():
#     if val>maxi:
#         maxi=val
#         char=key
# print(char)

# #write a program to print the num which is repeated for more no of times in list
# arr=[1,2,3,1,2,1,1]
# dic={}
# for i in arr:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# maxi=0
# cnt=0
# for key,val in dic.items():
#     if val > maxi:
#         maxi=val
#         cnt=key
# print(cnt)


#write a progeam to check the given string is palindrome or not if it is palindrome then return str as it is else return the rev str
n='mam'
res=lambda n: n if n==n[::-1] else n[::-1]
print(res(n))
#wrp to add min of two num max of 5

#write a program to remove duplicate values from dic
# dic={'a':10,'b':20,'c':10,'d':30}
# for key,value in dic.items():

inp='how are you'
string=inp.split()
inp.map()

