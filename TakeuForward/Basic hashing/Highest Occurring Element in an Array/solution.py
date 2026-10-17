class Solution:
    def secondMostFrequentElement(self, nums):
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        maxkey=0
        maxval=0
        secmaxval=0
        secmaxkey=0
        for key,value in hash.items():
            if maxval>value:
                secmaxval=maxval
                maxval=value
                secmaxkey=maxkey
                maxkey=key
            elif secmaxval <value and value!=maxval:
                secmaxval=value
                secmaxkey=key
            return secmaxkey