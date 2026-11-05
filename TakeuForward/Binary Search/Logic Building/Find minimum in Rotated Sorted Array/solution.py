class Solution:
    def findMin(self, arr):
        low=0
        high=len(arr)-1
        mini=float('inf')
        while low<=high:
            mid=(low+high)>>1
            if arr[low]<=arr[mid]:
                mini=min(mini,arr[low])
                low=mid+1
            else:
                mini=min(mini,arr[mid])
                high=mid-1
        return mini