class Solution:
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        position=len(nums)
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]>=target:
                position=mid
                high=mid-1
            else:
                low=mid+1
        return position