# Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

#Method 1
def leaf_list1(root, res=[]):
  if root is None:
    return []
  
  if root.left is None and root.right is None:
    return [root.val, *res]
  
  left = leaf_list1(root.left, res)
  right = leaf_list1(root.right, res)

  res = [*left, *right]
  return res

#Method 2
def leaf_list2(root):
  if not root:
    return [] 
  
  if not root.left and not root.right:
    return [root.val] 
  
  return leaf_list2(root.left) + leaf_list2(root.right)
  
  
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

