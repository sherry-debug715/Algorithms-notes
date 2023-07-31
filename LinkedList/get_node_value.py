# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def get_node_value(head, index): #25ms
#   counter = 0
#   current = head
#   while current is not None:
#     if counter==index:
#       return current.val
#     current = current.next
#     counter+=1
#   return None

# def get_node_value(head, index, counter=0): #43ms
#   if head is None:
#     return None
#   if counter==index:
#     return head.val
#   return get_node_value(head.next, index, counter+1)

def get_node_value(head, index): #45ms
  if head is None:
    return None
  if index==0:
    return head.val
  return get_node_value(head.next, index-1)



  



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 2) # 'c'