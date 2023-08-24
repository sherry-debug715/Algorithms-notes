# Description
# Given a binary tree, return all root-to-leaf paths.
# Input：{1,2,3,#,5}
# Output：["1->2->5","1->3"]
# Explanation：
#    1
#  /   \
# 2     3
#  \
#   5

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
    @return: all root-to-leaf paths
             we will sort your return value in output
    """
    def binary_tree_paths(self, root: TreeNode) -> List[str]:
        output = []
        self._binary_tree_paths(root, [root], output)
        return output
    
    def _binary_tree_paths(self, root, single_path, output):
        if not root:
            return 
        
        if not root.left and not root.right:
            output.append("->".join([str(n.val) for n in single_path]))
        
        single_path.append(root.left) 
        self._binary_tree_paths(root.left, single_path, output) 
        # backtracking for variable path, this step is important, for example #             1
        #           /    \
        #          2     3
        #        / \     /\
        #     None  5 None None
        #          /\
        #      None None
        # when root == node 2, None is appended to single_path list, [1, 2, None], then we hit line 33 and return, if we don't pop None out of the single_path list, we will end us with "1->2->None->5"
        single_path.pop() 

        single_path.append(root.right) 
        self._binary_tree_paths(root.right, single_path, output) 
        single_path.pop()
        