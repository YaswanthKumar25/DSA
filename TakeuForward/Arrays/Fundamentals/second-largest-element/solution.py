class Solution:
    def secondLargestElement(self, nums):
        maxi=float('-inf')
        secmaxi=float('-inf')
        for i in nums:
            if i > maxi:
                secmaxi=maxi
                maxi=i
            elif i > secmaxi and i != maxi:
                secmaxi=i
        return -1 if  secmaxi==float('-inf') else secmaxi
        