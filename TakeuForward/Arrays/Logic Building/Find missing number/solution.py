class Solution:
    def missingNumber(self, nums):
        sum_=0
        for i in range(len(nums)+1):
            sum_+=i
        return sum_-sum(nums)