class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
def insert(arr):
    head=ListNode(arr[0])
    temp=head
    for i in range(1,len(arr)):
        temp.next=ListNode(arr[i])
        temp=temp.next
    return head

arr=[1,2,3,4,5]
head=insert(arr)

def traverse(head):
    temp=head
    while temp:
        print(temp.val,end=" ")
        temp=temp.next


def insert_athead(head):
    new_node=ListNode(0)
    new_node.next=head
    head=new_node
    return head
insert_head=insert_athead(head)

def insert_tail(head):
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=ListNode(6)
    return head
    
def insert_delhead(head):
    head=head.next
    return head


def del_tail(head):
    temp=head
    while temp.next:
        temp=temp.next
    return head

dell_tail=del_tail(head)
traverse(dell_tail)
