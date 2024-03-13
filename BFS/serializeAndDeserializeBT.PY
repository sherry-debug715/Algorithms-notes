# Lintcode problem 7: https://www.lintcode.com/problem/7/

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if not root:
            return None

        tree = []
        queue = collections.deque([root])

        while queue:
            cur = queue.popleft()
            tree.append(str(cur.val) if cur else "#")
            if cur:
                queue.append(cur.left)
                queue.append(cur.right) 
        result = " ".join(tree)
        return " ".join(tree)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        if not data:
            return None 
        
        nodes = [TreeNode(val) if val != "#" else None for val in data.split()]
        root = nodes[0]
        fast_idx, slow_idx = 1, 0
        queue = [root]
        # print("root", root.val)
        while slow_idx < len(queue):
            cur_node = queue[slow_idx]
            slow_idx += 1

            cur_node.left = nodes[fast_idx]
            cur_node.right = nodes[fast_idx + 1]
            fast_idx += 2

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right) 
        
        return root