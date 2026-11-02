class Solution:
    def search(self, nums, target):
        i=0
        j=len(nums)-1
        while i <=j:
            mid=(i+j)>>1
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return -1
        

