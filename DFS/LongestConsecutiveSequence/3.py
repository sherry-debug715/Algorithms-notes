"""
Lintcode problem 619: https://www.lintcode.com/problem/619/
"""

"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        max_path, _, _ = self._longestConsecutive3(root)
        return max_path
    
    def _longestConsecutive3(self, root):
        if not root:
            return 0, 0, 0 
        
        max_path, max_increase, max_decrease = 0, 0, 0
        for node in root.children:
            child_maxPath, child_up, child_down = self._longestConsecutive3(node) 

            max_path = max(max_path, child_maxPath)
            if node.val + 1 == root.val:
                max_decrease = max(max_decrease, child_down + 1) 
            if node.val - 1 == root.val:
                max_increase = max(max_increase, child_up + 1) 
            
            max_path = max(max_path, max_increase + max_decrease + 1)
        
        return max_path, max_increase, max_decrease