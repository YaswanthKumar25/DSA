class Solution:
    def majorityElementTwo(self, nums):
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        n=(len(nums)//3)
        arr=[]
        for keys,values in hash.items():
            if values>n:
                arr.append(keys)
        return arr
            

        