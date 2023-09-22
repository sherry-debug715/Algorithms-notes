"""
Lintcode problem 102: https://www.lintcode.com/problem/102/
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
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    """
    Edge case:
        if linked list is empty, return False
    
    Initialize a pointer, slow, set it to head 
    Initialize a pointer, fast, set it to head.next 

    while fast is not None:
        set slow to slow.next 
        set fast to fast.next.next 
        if fast.val == slow.val:
            break 
    
    if not fast:
        return False 
    else:
        return True 
    """
    def hasCycle(self, head):
        if not head:
            return False 

        slow = head 
        fast = head 

        while fast and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 
            if fast == slow:
                return True 

        return False