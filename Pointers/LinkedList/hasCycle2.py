"""
lintcode problem 103: https://www.lintcode.com/problem/103/
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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        if not head or head.next is None:
            return None 
        
        slow, fast = head, head.next 
        while fast and fast.next and id(slow) != id(fast):
            slow = slow.next 
            fast = fast.next.next 
        
        if fast is None or fast.next is None:
            return None 
        
        new = head 
        while new != slow.next:
            new = new.next
            slow = slow.next 

        return new  