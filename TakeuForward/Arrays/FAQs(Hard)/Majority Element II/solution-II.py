class Solution:
    def majorityElementTwo(self, nums):
        cnt1=cnt2=0
        ele1=ele2=None
        for i in nums:
            if i == ele1:
                cnt1 += 1
            elif i == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = i
                cnt1 = 1
            elif cnt2 == 0:
                ele2 = i
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        n=len(nums)//3
        ans=[]
        cnt1=cnt2=0
        for i in nums:
            if i == ele1:
                cnt1+=1
            elif i == ele2:
                cnt2+=1
        if cnt1>n:
            ans.append(ele1)
        if cnt2>n:
            ans.append(ele2)
        return ans

        