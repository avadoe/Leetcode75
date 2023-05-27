def deleteMiddleNode(head):
    if not head or not head.next:
        return None
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    fast = head
    while fast.next is not slow:
        fast = fast.next
        
    fast.next = slow.next
    return head