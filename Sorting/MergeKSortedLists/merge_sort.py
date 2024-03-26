# Lintcode problem 104: https://www.lintcode.com/problem/104/


# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# Time: O(NlogK)
# Space: O(1)
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None 
        
        return self.merge_sort(0, len(lists) - 1, lists) 
    
    def merge_sort(self, start, end, lists):
        if start >= end:
            return lists[start]

        mid = (start + end) // 2

        left = self.merge_sort(start, mid, lists)
        right = self.merge_sort(mid + 1, end, lists) 
        return self.merge(left, right, lists) 
    
    def merge(self, head1, head2, lists):
        dummy = ListNode(None) 
        cur = dummy 

        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next 
            else:
                cur.next = head2 
                head2 = head2.next 
            cur = cur.next  
        
        if head1:
            cur.next = head1 
        if head2:
            cur.next = head2 
        
        return dummy.next

