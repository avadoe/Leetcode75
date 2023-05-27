def oddEven(head):
    if not head: return None
    if not head.next: return head
    odd = head
    even = head.next
    
    evenStart = even
    
    while odd.next and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
        
    odd.next = evenStart
    if not odd.next:
        even.next = None
        
    return head