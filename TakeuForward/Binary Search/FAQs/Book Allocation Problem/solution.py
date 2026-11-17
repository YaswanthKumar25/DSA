class Solution:
    def findPages(self, nums, m):
        if len(nums)<m:
            return -1
        left=max(nums)
        right=sum(nums)
        while left <= right:
            mid=(left+right)>>1
            noOfStudents=self.cntstudents(nums,mid,m)
            if noOfStudents>m:
                left=mid+1
            else:
                right=mid-1
        return left

        
    def cntstudents(self,nums,size,m):
        cnt=1
        maxsize=0
        for i in range(len(nums)):
            if (maxsize+nums[i])<=size:
                maxsize+=nums[i]
            else:
                cnt+=1
                maxsize=nums[i]
        return cnt

       