class Solution:
    def twoSum(self, nums, target):
        hash={}
        for ind,val in enumerate(nums):
            requ=target-val
            if  requ in hash:
                return [hash[requ],ind]
            else:
                hash[val]=ind       