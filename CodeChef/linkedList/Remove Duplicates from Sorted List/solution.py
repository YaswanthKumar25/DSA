'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.next = None
'''

class Solution:
    def removeDuplicates(self, head):
        # code here
        temp=head
        while temp and temp.next:
            if temp.data==temp.next.data:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head