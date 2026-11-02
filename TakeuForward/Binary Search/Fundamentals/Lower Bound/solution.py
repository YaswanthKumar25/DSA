class Solution:
    def lowerBound(self, nums, x):
        low=0
        high=len(nums)-1
        lower=len(nums)
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]>=x:
                lower=mid
                high=mid-1
            else:
                low=mid+1
        return lower
       


