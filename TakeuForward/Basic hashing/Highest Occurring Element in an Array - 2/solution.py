class Solution:
    def secondMostFrequentElement(self, nums):
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        maxval = secmaxval = -1
        maxkey = secmaxkey = -1
        freq=(sorted(freq.items()))
        for i in freq:
            if i[1]>maxkey:
                secmaxval=maxval
                secmaxkey=maxkey
                maxkey=i[1]
                maxval=i[0]
            elif i[1]>secmaxkey and i[1]!=maxkey:
                secmaxkey=i[1]
                secmaxval=i[0]
        return secmaxval
