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
        
        # find the tail of linked list A
        pointerA = headA
        while pointerA.next:
            pointerA = pointerA.next 
        
        # connect tail of linked list A with head of linked list B
        pointerA.next = headB 

        # look for entrance of the formed linked list circle 
        slow, fast = headA, headA.next 
        while fast and fast.next and id(slow) != id(fast):
            if fast is None or fast.next is None:
                return None 
            slow = slow.next
            fast = fast.next.next 
        
        new = headA
        while slow.next != new:
            slow = slow.next
            new = new.next 
        
        return new 