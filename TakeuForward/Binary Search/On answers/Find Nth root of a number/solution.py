class Solution:
    def nthRoot(self, n, m):
        if m==0:
            return 0
        low=1
        high=m
        while low<=high:
            mid=(low+high)>>1
            res=(mid**n)
            if res==m:
                return mid
            if res >m:
                high=mid-1
            else:
                low=mid+1 
        return -1
