class Solution:
    def moveZeroes(self, nums):
        zero=None
        for i in range(len(nums)):
            if nums[i]==0 and zero == None:
                zero=i
            if zero!=None and nums[i]!=0:
                nums[zero],nums[i]=nums[i],nums[zero]
                zero+=1
        return nums