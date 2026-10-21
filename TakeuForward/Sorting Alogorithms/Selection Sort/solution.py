class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            mini=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[mini]:
                    mini=j
            nums[i],nums[mini]=nums[mini],nums[i]
        return nums