"""
Lintcode problem 380: https://www.lintcode.com/problem/380/
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    """
    Edge case:
    1. if either one of head is None, return None 

    traverse through linked list A, to find tail. Reference tail.next to headB

    Initialize a pointer, slow, set it to headA
    Initialize a pointer, fast, set it to headA 
    while fast.next is not None:
        slow = slow.next
        fast = fast.next.next 
        if slow == fast:
            break 
    
    if fast.next is None:
        return None 
    
    while head != slow:
        head = head.next
        slow = slow.next 
    
    return slow 
    """
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None 
        
        cur = headA
        while cur.next:
            cur = cur.next 
        cur.next = headB 

        slow = headA 
        fast = headA

        while fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                break 
        
        if fast.next is None:
            return None 
        
        head = headA
        while head != slow:
            head = head.next 
            slow = slow.next 
        
        return slow 