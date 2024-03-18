# Lintcode problem 95: https://www.lintcode.com/problem/95

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

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    # when using in-order tranverse on a valid BST, the number should be in ascending order.
    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        self.is_valid = True 
        self.lastVal = None 
        self.validateBST(root)
        return self.is_valid 
    
    def validateBST(self, root):
        if not root:
            return 
        
        self.validateBST(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.is_valid = False 
            return 
        self.lastVal = root.val 
        self.validateBST(root.right)
