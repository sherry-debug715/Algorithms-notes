#Lintcode problem 129: https://www.lintcode.com/problem/129/
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    """
    rehashing function:
    Initialize a Integer, size, to store new hashTable size
    Initialize a new list, new_hashTable, it has double the size of the old hashTable 
    Iterate over the old hashTable, using node:
        check if node is None, if not:
            WHILE curNode is not None:
                pass val, and new_hashTable into a helper function, insertion, to insert the new node 
                into new_hashTable
    return new_hashTable

    insertion function:
    pass node val into hashcode functioin to get new key.
    Create a new ListNode object of node val
    check if new_hashTable[new key] is None
    if None: new_hashTable[new key] = ListNode
    else:
        create a helper function, add_to_linkedlist, that takes in the following argument:
        1. new key. 2. new_hashTable 3. newNode

    add_to_linkedlist function: 1. new key. 2. new_hashTable
    Get the head of the linkedlist, new_hashTable[new key]
    check if head.next is None: add newNode to head.next 
    else: iterate through the linkedlist, until cur.next is None, then point cur.next at newNode

    """
    
    def hashcode(self, val, capacity):
        return val % capacity

    def rehashing(self, hashTable):
        size = len(hashTable) * 2
        new_hashTable = [None] * size 

        for node in hashTable:
            if node:
                cur = node
                while cur:
                    self.insertion(cur.val, new_hashTable, size)
                    cur = cur.next

        return new_hashTable 
    
    def insertion(self, val, new_hashTable, size):
        key = self.hashcode(val, size) 
        new_node = ListNode(val) 

        if new_hashTable[key] is None:
            new_hashTable[key] = new_node
            return 
        else:
            self.add_to_linkedList(key, new_hashTable, new_node)
            return 
    
    def add_to_linkedList(self, key, new_hashTable, new_node):
        head = new_hashTable[key] 
        if head.next is None:
            head.next = new_node
            return 
        else:
            cur = head
            while cur.next:
                cur = cur.next 
            cur.next = new_node
            return 
