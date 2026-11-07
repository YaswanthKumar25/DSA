class Solution:
    def shipWithinDays(self, weights, days):
        low=min(weights)
        high=sum(weights)
        ans=0
        while low<=high:
            mid=(low+high)>>1
            val=self.minvalue(weights,mid,days)
            if val:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
                
    def minvalue(self, nums, capacity, days):
        day = 0
        i = 0
        while day < days:
            curr_capacity = capacity
            while i < len(nums) and curr_capacity >= nums[i]:
                curr_capacity -= nums[i]
                i += 1
            day += 1
        return i == len(nums)