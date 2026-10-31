class Solution:
    def maxSubArray(self, nums):
        sum_=float('-inf')
        maxi=0
        for i in nums:
            maxi+=i
            sum_=max(sum_,maxi)
            if maxi<=0:
                maxi=0
        return sum_