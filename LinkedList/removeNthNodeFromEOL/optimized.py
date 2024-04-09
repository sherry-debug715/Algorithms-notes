# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time: O(N)
# Space: O(1)
# The following pattern is used to look for the last n node from a list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next 

        dummy = ListNode(0, head) 
        slow, fast = dummy, dummy 
        delta = n

        while delta >= 0 and fast is not None:
            fast = fast.next
            delta -= 1 

        # slow will stop at node_to_remove.prev
        while fast is not None:
            slow = slow.next
            fast = fast.next 

        # if list has one node, slow == dummy.
        slow.next = slow.next.next 
        return dummy.next  


        