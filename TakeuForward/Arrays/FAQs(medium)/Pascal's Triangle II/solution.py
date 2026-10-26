class Solution:
    def pascalTriangleII(self, r):
        ans=[]
        for i in range(r):
            ans.append(self.ncr(r-1,i))
        return ans
            
    def ncr(self,row,col):
        res=1
        for i in range(col):
            res=res*(row-i)
            res=res//(i+1)
        return res