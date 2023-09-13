"""
LintCode problem 960: https://www.lintcode.com/problem/960
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 
        self.prev = None

class DataStream:
    def __init__(self):
        self.visited = {}
        self.head = None 
        self.tail = None
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num): 
        if num in self.visited:
            self.remove(num)
        else:
            new_node = Node(num)
            if not self.head:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node 
                new_node.prev = self.tail
                self.tail = new_node 

            self.visited[num] = new_node 

    def remove(self, num):
        node_to_remove = self.visited[num]
        if node_to_remove:
            if node_to_remove == self.head:
                self.head = self.head.next
                # if node to remove was not the only node stored in the linked list
                if self.head:
                    self.head.prev = None
            elif node_to_remove == self.tail:
                self.tail = self.tail.prev 
                if self.tail:
                    self.tail.next = None
            else:
                prev = node_to_remove.prev 
                next_node = node_to_remove.next 
                prev.next = next_node 
                next_node.prev = prev 
        self.visited[num] = None 
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        return self.head.val if self.head else -1