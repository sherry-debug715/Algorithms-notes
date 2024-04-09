# Leetcode problem 19: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next 
        
        list_length = self.count_length(head) # O(N)
        new_n = list_length - n 
        if new_n == 0:
            return head.next
        counter = 1 
        cur = head 
        while counter < new_n: # O(N)
            cur = cur.next 
            counter += 1
        new_next = cur.next.next 
        cur.next = new_next 

        return head
    
    def count_length(self, head):
        counter = 0
        cur = head

        while cur:
            cur = cur.next
            counter += 1 
        
        return counter

        