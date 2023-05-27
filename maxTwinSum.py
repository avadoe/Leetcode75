def pairSum(head):
    if not head:
        return 0
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    # slow is the head of the second half of the linked list at the moment
    prev = None
    while slow is not None:
        nextNode = slow.next
        slow.next = prev
        prev = slow
        slow = nextNode
        
    second_half_head = prev
    second = second_half_head
    first = head
    
    max_sum = 0
    while first and second:
        max_sum = max(max_sum, first.val + second.val)
        first = first.next
        second = second.next
        
    return max_sum 