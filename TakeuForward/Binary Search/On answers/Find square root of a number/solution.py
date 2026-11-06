class Solution:
    def floorSqrt(self, n: int) -> int:
        low=0
        high=n
        ans=None
        while low<=high:
            mid=(low+high)>>1
            if (mid*mid)<=n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans