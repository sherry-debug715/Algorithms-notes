# Lintcode problem 482: https://www.lintcode.com/problem/482/

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
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def level_sum(self, root: TreeNode, level: int) -> int:
        if not root:
            return 0
        
        res = []
        self.dfs(root, level, 1, res)
        return sum(res)
    
    def dfs(self, node, level, cur_level, res):
        if not node:
            return 
        
        if cur_level == level:
            res.append(node.val)
            return 
        
        if node.left:
            self.dfs(node.left, level, cur_level + 1, res)
        if node.right:
            self.dfs(node.right, level, cur_level + 1, res)
