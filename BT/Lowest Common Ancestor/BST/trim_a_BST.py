# Lintcode problem 701: https://www.lintcode.com/problem/701/

from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# Time: O(n)
# Space: O(N) where in worst case, N is the total amount of tree nodes 
class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trim_b_s_t(self, root: TreeNode, minimum: int, maximum: int) -> TreeNode:
        if not root:
            return None 
        
        def trim(node):
            if not node:
                return None 
            
            if node.val < minimum:
                return trim(node.right) 
            elif node.val > maximum:
                return trim(node.left) 
            else:
                node.left = trim(node.left)
                node.right = trim(node.right) 
                return node  
        
        return trim(root)
