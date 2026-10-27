class Solution:
    def sortZeroOneTwo(self, nums):
        i=j=0
        k=len(nums)-1
        while j <=k:
            if nums[j]==0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            elif nums[j]==1:
                j+=1
            else:
                nums[k],nums[j]=nums[j],nums[k]
                k-=1
        