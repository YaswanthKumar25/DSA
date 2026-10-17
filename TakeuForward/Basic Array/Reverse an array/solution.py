class Solution:
    def reverse(self, arr: list, n: int) -> None:
        i=0
        j=len(arr)-1
        while i <=j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        