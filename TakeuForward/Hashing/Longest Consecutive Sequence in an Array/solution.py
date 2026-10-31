class Solution:
    def longestConsecutive(self, nums):
        hash=set(nums)
        maxcnt=0
        for i in hash:
            if i-1 in hash:
                pass
            else:
                cnt=0
                while i in hash:
                    cnt+=1
                    i+=1
                maxcnt=max(cnt,maxcnt)
        return maxcnt
