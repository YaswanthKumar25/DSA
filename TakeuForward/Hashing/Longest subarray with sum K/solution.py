class Solution:
    def longestSubarray(self, nums, k):
        # code here
        hash={0:-1}
        maxi=0
        sum_=0
        for i in range(len(nums)):
            sum_+=nums[i]
            target=sum_-k
            if target in hash:
                maxi=max(maxi,i-hash[target])
            if sum_ not in hash:
                hash[sum_]=i
        return maxi
            
