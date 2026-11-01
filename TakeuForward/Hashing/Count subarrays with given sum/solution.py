class Solution:
    def subarraySum(self, nums, k):
        hash={0:1}
        sum_=0
        cnt=0
        for i in range(len(nums)):
            sum_+=nums[i]
            if (sum_-k) in hash:
                cnt+=hash[sum_-k]
            hash[sum_]=hash.get(sum_,0)+1
        return cnt