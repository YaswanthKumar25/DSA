class Solution:
    def linearSearch(self, nums, target):
        for ind,val in enumerate(nums):
            if val == target:
                return ind
        return -1