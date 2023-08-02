# Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def add_lists(head_1, head_2):
#   cur_1 = head_1
#   cur_2 = head_2
#   dummy_head = Node(None)
#   prev = dummy_head
#   carry = 0
# # add cur_1 and cur_2
# # if cur_1 + cur_2 >= 10: carry = 1
#   while cur_1 is not None or cur_2 is not None or carry != 0:
#     if cur_2 is None:
#       cur_2 = Node(0)
#     if cur_1 is None:
#       cur_1 = Node(0)
      
#     new_node_val = cur_1.val + cur_2.val
#     if new_node_val+carry >= 10:
#       new_node_val = (cur_1.val + cur_2.val) - 10 + carry
#       carry = 1
#     else:
#       new_node_val = cur_1.val + cur_2.val + carry
#       carry = 0
#     new_node = Node(new_node_val)
#     prev.next = new_node
#     prev = new_node
    
#     cur_1 = cur_1.next
#     cur_2 = cur_2.next
    
#   return dummy_head.next

# def add_lists(head_1, head_2, carry=0):
#   if head_1 is None and head_2 is None and carry == 0:
#     return None
  
#   val_1 = head_1.val if head_1 else 0
#   val_2 = head_2.val if head_2 else 0
#   print('VAL1', val_1)
#   print('VAL2', val_2)

#   new_node_val = val_1+val_2+carry if val_1+val_2+carry<10 else val_1+val_2-10+carry
#   print('NEW NODE VAL', new_node_val)
  
#   carry = 1 if val_1+val_2+carry>=10 else 0
#   print('CARRY', carry)
#   new_node = Node(new_node_val)
#   next_1 = head_1.next if head_1 else None
#   next_2 = head_2.next if head_2 else None
#   new_node.next = add_lists(next_1, next_2, carry)
  
#   return new_node

def add_lists(head_1, head_2):
  dummy_head = Node(None)
  pointer = dummy_head
  carry = 0
  current_1 = head_1
  current_2 = head_2
  while current_1 or current_2 or carry:
    val_1 = current_1.val if current_1 else 0
    val_2 = current_2.val if current_2 else 0
    sum_up = val_1 + val_2 + carry
    carry = 1 if sum_up > 9 else 0
    digit = sum_up % 10
    print(digit)
    pointer.next = Node(digit)
    pointer = pointer.next
    if current_1:
      current_1 = current_1.next
    if current_2:
      current_2 = current_2.next 
  return dummy_head.next
      
  
