class Solution:
    def isSorted(self, nums):
        i=0
        while i <len(nums)-1:
            if nums[i]<=nums[i+1]:
                i+=1
            else:
                return False
        return True