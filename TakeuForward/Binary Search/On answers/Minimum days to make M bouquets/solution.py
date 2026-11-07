class Solution:
    def roseGarden(self, n, nums, k, m):
        #your code goes here
        if (m*k)>n:
            return -1
        low=min(nums)
        high=max(nums)
        ans=-1
        while low<=high:
            mid=(low+high)>>1
            day=self.possible(nums,mid,k,m)
            if day:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def possible(self,nums,day,k,m):
        cnt=0
        NoOf=0
        for i in nums:
            if i<=day:
                cnt+=1
            else:
                NoOf+=(cnt//k)
                cnt=0
        NoOf+=(cnt//k)
        return True if (NoOf)>=m else False