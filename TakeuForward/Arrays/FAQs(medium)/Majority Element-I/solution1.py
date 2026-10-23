class Solution:
    def majorityElement(self, nums):
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        maxi=0
        key=None
        for keys,values in hash.items():
            if values>maxi:
                key=keys
                maxi=values
        return key
            

            