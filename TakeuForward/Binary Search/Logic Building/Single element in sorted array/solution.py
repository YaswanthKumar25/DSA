class Solution:
    def singleNonDuplicate(self, nums):
        if len(nums)==1:
            return nums[0]
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)>>1
            if mid == len(nums)-1:
                if nums[mid-1]!=nums[mid]:
                    return nums[mid]
            if mid == 0:
                if nums[mid+1]!=nums[mid]:
                    return nums[mid]

            if nums[mid-1]!=nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid % 2 == 1:
                if nums[mid-1]==nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[mid-1]==nums[mid]:
                    high=mid-1
                else:
                    low=mid+1


       