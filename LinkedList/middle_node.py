# You're given a Linked list with at least one node. Write a function that returns the middle node of the Linked List. If there are two middle nodes(i.e. an even length list), your function should return the second of these nodes.

# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null if it's the tail of the list

# method 1:
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

 # Time: O(n) + O(1) + O(n/2) Space: O(1) + O(n/2)
def middleNode(linkedList):
    # Write your code here.
    total_nodes = count_nodes(linkedList)
    mid = total_nodes // 2
    return find_mid_node(linkedList, mid)

# Time: O(n) Space: O(1)
def count_nodes(head): 
    counter = 0
    cur = head
    while cur:
        counter += 1
        cur = cur.next
    return counter

#Time: O(n/2) Space: O(n/2) stack
def find_mid_node(head, idx): 
    if idx == 0:
        return head

    return find_mid_node(head.next, idx - 1)

# method 2: the hare and tortoise method or Floyd's cycle detection algorithm

# the fast pointer is moving 2 steps at a time, therefore, after n times, it would have moved 2n steps

# the slow pointer is moving 1 step at a time, after moving n times, it would have moved n steps.

# when fast pointer reach the end of the linked list, the slow pointer would have stopped at the half of location, which is the middle node. 
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time: O(n) Space: O(1)
def middleNode(linkedList):
    fast_pointer = linkedList
    slow_pointer = linkedList

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer


    
    

    
