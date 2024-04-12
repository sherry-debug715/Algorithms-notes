# Lintcode problem 134: https://www.lintcode.com/problem/134/

class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # if key doesn't exist in map, return -1 
        if key not in self.map:
            return -1 
        # else, locate the node by accessing the map, delete the node then add 
        # it before tail.
        node = self.map[key]
        self.delete_node(node)
        self.add_to_tail(node)
        return node.val 

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # if key already exist - delete the node then add the new node 
        # else - check capacity 
            # if reach capacity - delete head.next, then add new node the tail.prev 
            # else - add to map, add to tail.prev 
        newNode = ListNode(value, key)
        if key in self.map:
            self.delete_node(self.map[key])
            self.add_to_tail(newNode) 
            self.map[key] = newNode 
        else:
            if len(self.map.values()) == self.capacity:
                del self.map[self.head.next.key] 
                self.delete_node(self.head.next) 

            self.map[key] = newNode 
            self.add_to_tail(newNode)
    
    def delete_node(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev 
    
    def add_to_tail(self, node):
        node.prev = self.tail.prev 
        self.tail.prev.next = node 
        node.next = self.tail 
        self.tail.prev = node 
