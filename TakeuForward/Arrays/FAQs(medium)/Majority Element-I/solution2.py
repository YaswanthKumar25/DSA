class Solution:
    def majorityElement(self, nums):
        cnt=0
        val=None
        for i in range(len(nums)):
            if val == None:
                cnt+=1
                val=nums[i]
            elif val==nums[i]:
                cnt+=1
            elif val!=nums[i] and cnt!=0:
                cnt-=1
            elif val!=nums[i] and cnt==0:
                cnt+=1
                val=nums[i]
        return val
            

            