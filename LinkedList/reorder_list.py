# Leetcode problem 143: https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None 
        
        mid = self.find_mid(head) # O(N)
        cur2 = self.reverseList(mid.next) #O(half of N)
        cur1 = head
        mid.next = None

        while cur1 and cur2: # O(N)
            cur1_next = cur1.next
            cur2_next = cur2.next
            cur1.next = cur2
            cur2.next = cur1_next
            cur1 = cur1_next
            cur2 = cur2_next
        
        return head
    
    def find_mid(self, head):
        slow, fast = head, head.next 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    
    def reverseList(self, mid_next):
        prev, cur = None, mid_next 

        while cur:
            cur_next = cur.next 
            cur.next = prev
            prev = cur 
            cur = cur_next 
        
        return prev 
        