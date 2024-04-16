# Lintcode problem 376: https://www.lintcode.com/problem/376/

from typing import (
    List,
)
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
# Time: O(N)
# Space: O(H)
class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return [] 
        
        res = []
        self.dfs(root, res, [root.val], target)
        return res 
    
    def dfs(self, node, res, path, target):
        if not node:
            return
        
        if not node.left and not node.right and sum(path) == target:
            res.append([*path])
            return 
        
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, res, path, target)
            path.pop()
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, res, path, target) 
            path.pop()
