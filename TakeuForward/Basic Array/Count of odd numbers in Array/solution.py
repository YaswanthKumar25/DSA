class Solution:
    def countOdd(self, arr, n):
        cnt=0
        for i in arr:
            if i % 2==1:
                cnt+=1
        return cnt