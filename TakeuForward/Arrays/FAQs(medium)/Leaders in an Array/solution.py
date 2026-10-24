class Solution:
    def leaders(self, nums):
        maxi=float('-inf')
        leaders=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>maxi:
                leaders.append(nums[i])
                maxi=nums[i]
        return leaders[::-1]