class Solution:
    def rotateArrayByOne(self, nums):
        first=[nums[0]]
        second=nums[1:]
        final=second+first
        for i in range(len(nums)):
            nums[i]=final[i]
        