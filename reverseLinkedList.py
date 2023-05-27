def reverseLinkedList(self, head):
    if not head or not head.next:
        return head
    
    prev = None
    curr = head
    
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    return prev

