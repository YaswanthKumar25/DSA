class Solution:
    def findKRotation(self, nums):
        low=0
        high=len(nums)-1
        mini=float('inf')
        ind=-1
        while low<=high:
            mid=(low+high)>>1
            if nums[low]<=nums[mid]:
                if nums[low]<mini:
                    mini=nums[low]
                    ind=low
                low=mid+1
            else:
                if nums[mid]<mini:
                    mini=nums[low]
                    ind=mid
                high=mid-1
        return ind