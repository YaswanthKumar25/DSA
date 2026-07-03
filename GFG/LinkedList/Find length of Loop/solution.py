'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow=fast=head
        # if fast is None or fast.next is None:
        #     return head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                cnt=self.count(slow,fast)
                return cnt
        return 0
    def count(self,slow,fast):
        cnt=1
        fast=fast.next
        while slow!=fast:
            cnt+=1
            fast=fast.next
        return cnt
            
            