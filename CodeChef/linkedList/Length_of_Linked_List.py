# class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


def getLength(head):
    #write your code here...
    cnt=0
    while head:
        cnt+=1
        head=head.next
    return cnt