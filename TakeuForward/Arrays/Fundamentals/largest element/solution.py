class Solution:
    def largestElement(self, nums):
        maxi=float('-inf')
        for i in nums:
            maxi=max(maxi,i)
        return maxi
        