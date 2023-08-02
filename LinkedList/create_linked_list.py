# Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def create_linked_list(values):
#   dummy_head = Node(None)
#   prev = dummy_head
#   for i in values:
#     new_node = Node(i)
#     prev.next = new_node
#     prev = new_node
#   return dummy_head.next

# def create_linked_list(values, idx=0):
#   if idx == len(values):
#     return None
  
#   head = Node(values[idx])
#   head.next = create_linked_list(values, idx+1)
  
#   return head

# def create_linked_list(values):
#   if not len(values):
#     return None
  
#   head = Node(values[0])
  
#   head.next = create_linked_list(values[1:])
  
#   return head

# def create_linked_list(values_list):
#   if not len(values_list):
#     return None
#   head = Node(values_list[0])
#   tracker = head
#   for index in range(1,len(values_list)):
#     new_node = Node(values_list[index])
#     tracker.next = new_node
#     tracker = tracker.next
#   return head
  
  
  
  
    
    
