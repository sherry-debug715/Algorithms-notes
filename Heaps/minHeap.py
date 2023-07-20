# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        # find each parent node of the heap

        last_idx = len(array) - 1
        # made mistake of stopping range at len(array) - 1, this would stop the iteration before reaching the root node.
        for idx in range(1, len(array), 2):
            parent_idx = (last_idx - idx) // 2
            self.siftDown(parent_idx, array)
        return array
            
        

    def siftDown(self, idx, heap):
        # Write your code here.
        # find left child
        left_child_idx = (idx*2) + 1
        # find right child
        right_child_idx = (idx*2) + 2
        # find the children with smaller value
        if left_child_idx >= len(heap) and right_child_idx >= len(heap):
            return 
            
        if left_child_idx >= len(heap):
            min_idx = right_child_idx
        elif right_child_idx >= len(heap):
            min_idx = left_child_idx
        else:
            min_idx = left_child_idx if heap[left_child_idx] < heap[right_child_idx] else right_child_idx
        # compare heap[min_idx] with heap[idx], if heap[min_idx] is smaller swap, else return
        
        if heap[min_idx] > heap[idx]:
            return
        else:
            self.swapIdx(min_idx, idx, heap)
            self.siftDown(min_idx, heap)

    def siftUp(self, idx, heap):
        # Write your code here.
        # compare the value with the value of the parent node, if value < parent value, swap 
        # location
        if idx == 0:
            return 
        node_val = heap[idx]
        parent_idx = self.findParent(idx)
        if node_val >= heap[parent_idx]:
            return
        else:
            self.swapIdx(idx, parent_idx, heap)
            self.siftUp(parent_idx, heap)
        
            
    def peek(self):
        # Write your code here.
        return self.heap[0]

    # test case expect to return the removed value, and test is only testing removing the root from 
        # the heap, therefore, it doesn't allow any additional parameter given to the function.
    def remove(self):
        # Write your code here.
        # swap the removed node with the last node in the heap
        self.swapIdx(0, len(self.heap) - 1, self.heap)
        # pop off the node after swaping
        removed = self.heap.pop()
        # start siftDown
        self.siftDown(0, self.heap)

        return removed
        
    def insert(self, value):
        # Write your code here.
        # append the value to the array
        # siftUp the value until it finds the correct index
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        

    def findParent(self, idx):
        return (idx - 1) // 2

    def swapIdx(self, idx1, idx2, heap):
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]
