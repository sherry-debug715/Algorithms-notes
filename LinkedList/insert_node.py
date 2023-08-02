# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def insert_node(head, value, index):
#   count = 0
#   current = head
#   prev = None
#   while count < index:
#     prev = current
#     current = current.next
#     count += 1
#   # breakout of while loop:
#   # index is 0, add to head
#   # index is greater than the length of linked list, add to tail
#   # in the middle
#   new_node = Node(value) 
#   if index == 0:
#     new_node.next = head
#     return new_node
  
#   if current is None:
#     prev.next = new_node
#   else:
#     prev.next = new_node
#     new_node.next = current
  
#   return head

def insert_node(head, value, index):
  new_node = Node(value)
  
  if index == 0:
    new_node.next = head
    return new_node
    
  index_tracker = 0
  current = head
  prev = None
  
  while current:
    print('current', current.val)
    if index_tracker == index:
      prev.next = new_node
      new_node.next = current
    
    prev = current
    current = current.next
    index_tracker += 1
  print('index_tracker', index_tracker)
  if index == index_tracker:
    prev.next = new_node
  
  return head

# def insert_node(head, value, index, count=0):
#   new_node = Node(value)
#   if index == 0:
#     new_node.next = head
#     return new_node
  
#   if head is None:
#     return None
  
#   if index == count+1:
#     next = head.next
#     head.next = new_node
#     new_node.next = next
#     return
  
#   insert_node(head.next, value, index, count+1)
#   return head

# def insert_node(head, value, index):
#   counter = index
#   cur = head
#   new_node = Node(value)
  
#   if index == 0:
#     new_node.next = head
#     return new_node
  
#   while counter - 1 > 0:
#     cur = cur.next
#     counter -= 1
#   next = cur.next
#   cur.next = new_node
#   new_node.next = next
#   return head
  
  
    
  
    
