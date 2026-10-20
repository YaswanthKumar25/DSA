class Solution:
    def checkPrime(self, num):
        i=1
        cnt=0
        while i <=num:
            if num%i==0:
                cnt+=1
            i+=1
        return True if cnt == 2 else False
