class Solution:
    def find_kth_positive(self, arr, k):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)>>1
            missing=arr[mid]-(mid+1)
            if missing <k:
                low=mid+1
            else:
                high=mid-1
        return low+k
        
            