def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)
    
    # Edge case: If inserting at the very beginning (head)
    if position == 0:
        new_node.next = llist
        return new_node
        
    # Your existing correct logic for positions > 0
    temp = llist
    for i in range(position - 1):
        temp = temp.next
        
    next_node = temp.next
    temp.next = new_node
    new_node.next = next_node
    
    return llist