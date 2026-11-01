class Solution:
    def maxLength(self, arr):
        hash={0:-1}
        maxlen=0
        sum_=0
        for i in range(len(arr)):
            sum_+=arr[i]
            if sum_ in hash:
                maxlen=(max(maxlen,i-hash[sum_]))
            if sum_ not in hash:
                hash[sum_]=i
        return maxlen
