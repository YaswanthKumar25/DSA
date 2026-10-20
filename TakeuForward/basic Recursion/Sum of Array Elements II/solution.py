class Solution:
    def arraySum(self, nums):
        i=0
        sum_=0
        while i < len(nums):
            sum_+=nums[i]
            i+=1
        return sum_