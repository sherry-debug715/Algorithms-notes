"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq 
"""
By defining the __lt__ method for ListNode, you are essentially informing Python how to compare two ListNode instances whenever it encounters an operation requiring comparison. This definition is used implicitly by the heapq functions (such as heappush and heappop) when they need to compare the nodes to maintain the heap's order.

In the mergeKLists function:

heapq.heappush(heap, head) adds a ListNode to the heap. Python uses the __lt__ method to compare this node against others in the heap to find its correct position.
heapq.heappop(heap) removes and returns the smallest node from the heap. The __lt__ method is used to reorganize the remaining nodes in the heap after the smallest node is removed.
"""

ListNode.__lt__ = lambda x, y : x.val < y.val 

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    # Time: O(NlogK)
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        queue = []

        for head in lists:
            if head:
                heapq.heappush(queue, head) 

        dummy = ListNode(None)
        cur = dummy 
        while queue:
            node = heapq.heappop(queue)
            cur.next = node 
            cur = cur.next 
            if node.next:
                heapq.heappush(queue, node.next) 
        
        return dummy.next 



        

