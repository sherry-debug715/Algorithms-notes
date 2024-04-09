# Leetcode problem 138: https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Time: O(N)
# Space: O(N)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        initial_copy = {}
        cur = head
        # store original node and the relative copy into a hash map, each node at this point is not connected.
        while cur:
            copy = Node(cur.val)
            initial_copy[cur] = copy 
            cur = cur.next 
        
        # connect copied nodes with their next and random pointer.
        cur1 = head 
        while cur1:
            copy = initial_copy[cur1]
            # find cur1.next node
            copy_next = initial_copy[cur1.next] if cur1.next else None
            copy.next = copy_next 
            # find cur1.random node
            copy_random = initial_copy[cur1.random] if cur1.random else None
            copy.random = copy_random 
            
            cur1 = cur1.next 
        
        return initial_copy[head]
        
