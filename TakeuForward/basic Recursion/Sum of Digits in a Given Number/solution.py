class Solution:
    def addDigits(self, num):
        sum_=0
        if num <10:
            return num
        while num:
            sum_+=num%10
            num//=10
        return self.addDigits(sum_)

