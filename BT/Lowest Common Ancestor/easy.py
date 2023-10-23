"""
Lintcode problem 474: https://www.lintcode.com/problem/474/
"""

# useing hashset
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        if not root:
            return None 
        
        visited = set()

        cur = A
        while cur:
            visited.add(cur)
            cur = cur.parent 
        
        cur2 = B
        while cur2:
            if cur2 in visited:
                return cur2 
            visited.add(cur2)
            cur2 = cur2.parent 
