class Solution:
    def pascalTriangleIII(self, n):
        ans=[]
        for i in range(1,n+1):
            temp=[]
            for j in range(i):
                temp.append(self.ncr(i-1,j))
            ans.append(temp)
        return ans
    
    def ncr(self,row,col):
        res=1
        for i in range(col):
            res=res*(row-i)
            res=res//(i+1)
        return res

