# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def depth_first_values(root):
#   stack = []
#   nodes = [root]
#   if root is None:
#     return stack
#   while len(nodes):
#     current = nodes.pop()
#     stack.append(current.val)
    
#     if current.right:
#       nodes.append(current.right)
#     if current.left:
#       nodes.append(current.left)
    
#   return stack

def depth_first_values(root):
  if not root:
    return []

  left_val = depth_first_values(root.left)
  right_val = depth_first_values(root.right)
  
  return [root.val, *left_val, *right_val]

  
  
  
  


    
