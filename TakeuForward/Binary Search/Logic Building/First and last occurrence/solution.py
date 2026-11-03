class Solution:
    def searchRange(self, nums, target):
        first=self.first(nums,target)
        second=self.second(nums,target)
        return [first,second]

    def first(self,nums,target):
        low=0
        high=len(nums)-1
        ind=-1
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]==target:
                ind=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ind

    def second(self,nums,target):
        low=0
        high=len(nums)-1
        ind=-1
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]==target:
                ind=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ind