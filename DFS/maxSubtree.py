"""
lintcode problem 628: https://www.lintcode.com/problem/628/
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
    @return: the maximum weight node
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        _, _, max_subtree = self._find_subtree(root)
        return max_subtree 

    def _find_subtree(self, root):
        if not root:
            return 0, float("-inf"), root 
        
        left_sum, left_max, left_max_tree = self._find_subtree(root.left)
        right_sum, right_max, right_max_tree = self._find_subtree(root.right) 

        cur_sum = left_sum + right_sum + root.val
        cur_max = max(cur_sum, left_max, right_max) 

        # if current node is the current max subtree
        if cur_sum == cur_max:
            return cur_sum, cur_max, root 
        # if current left child is the current max subtree
        elif cur_max == left_max:
            return cur_sum, left_max, left_max_tree 
        elif cur_max == right_max:
            return cur_sum, right_max, right_max_tree 
    

