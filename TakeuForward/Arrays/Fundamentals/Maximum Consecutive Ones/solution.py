class Solution:
    def findMaxConsecutiveOnes(self, nums):
        cnt=0
        maxcnt=0
        for i in nums:
            if i == 1:
                cnt+=1
            else:
                cnt=0
            maxcnt=max(cnt,maxcnt)
        return maxcnt