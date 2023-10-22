"""
Lintcode problem 596: https://www.lintcode.com/problem/596/?fromId=161&_from=collection
"""

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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        self.min_sum = float("inf")
        self.minSum_node = None 
        self._find_subtree(root)  
        return self.minSum_node

    def _find_subtree(self, root):
        if root is None:
            return 0 
        
        left = self._find_subtree(root.left)
        right = self._find_subtree(root.right)
        cur_sum = left + right + root.val
        if cur_sum < self.min_sum:
            self.minSum_node = root
            self.min_sum = min(self.min_sum, cur_sum) 
            
        return cur_sum
   

