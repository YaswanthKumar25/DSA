class Solution:
    def pascalTriangleI(self, r, c):
        return self.ncr(r-1,c-1)

    def ncr(self,row,col):
        res=1
        for i in range(col):
            res=res*(row-i)
            res=res//(i+1)
        return res