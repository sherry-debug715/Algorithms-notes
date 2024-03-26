"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
"""
下面的方法采用自下而上，两两归并的倒三角形方式 
Time: O(NlogK)
Space: O(N)
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None 
        
        while len(lists) > 1:
            new_lists = [] 
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    new_head = self.merge_lists(lists[i], lists[i + 1])
                else:
                    new_head = lists[i] 
                new_lists.append(new_head) 
            lists = new_lists 
        
        return lists[0] 
    
    def merge_lists(self, head1, head2):
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
    