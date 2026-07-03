# Node is defined as:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def solve(head):
    #Return the number of critical points (integer)
    cnt=0
    prev=head
    temp=head.next
    while temp.next:
        if prev.val < temp.val > temp.next.val:
            cnt+=1
        elif prev.val > temp.val < temp.next.val:
            cnt+=1
        prev=temp
        temp=temp.next
    return cnt