class Solution:
    def upperBound(self, nums, x):
        low=0
        high=len(nums)-1
        upper=len(nums)
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]>x:
                upper=mid
                high=mid-1
            else:
                low=mid+1
        return upper
        