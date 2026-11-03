class Solution:
    def getFloorAndCeil(self, nums, x):
        ceil=floor=-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]<=x:
                ceil=nums[mid]
                low=mid+1
            if nums[mid]>=x:
                floor=nums[mid]
                high=mid-1
        return [ceil,floor]