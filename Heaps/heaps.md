* The binary heap data structure is __an array object__ that we can view as a nearly complete binary tree.

* Each node of the tree corresponds to an element from an array.

* Computation, given an index i from the heap where i is not the root node of the heap binary tree, or i != 0:

    * find parents: (i - 1) // 2
    * find left child: 2 * i + 1
    * find right child: 2 * i + 2

* There are __two__ types of binary heap, __min-heaps__ and __max-heaps__.

* max-heaps: Array[parent[i]] >= Array[i].
    * Meaning, the value of a node is at most the value of its parent, thus, the node with the largest value is stored at the root.


## Min-heap

* min-heaps: Array[parent[i]] <= Array[i]

### Build in functions 

#### Create a min-heap from a list

* heapq.heapify

Python provides a built-in module heapq for creating min-heap from a list in less time complexity. The function heapq.heapify(list) transforms a regular list to a heap, in-place, in linear time.

heapq module doesn't has a function that will convert a list into a max-heap.

```py
import heapq

nums = [4, 10, 3, 5, 1]

heapq.heapify(nums)

print(nums) # prints [1, 4, 3, 5, 10]
```

### remove the smallest value then re-organize the heap.

* heapq.heappop(heap)

```py
import heapq

nums = [4, 10, 3, 5, 1]

heapq.heapify(nums)

print(nums) # prints [1, 4, 3, 5, 10]

# Pop and return smallest element from heap
print(heapq.heappop(nums))  # Output: 1

# Heap after popping
print("Heap after popping: ", nums)  # Output: [3, 4, 10, 5]
```

### push a value onto the heap, while maintaining the heap invariant
```py
import heapq

# Initialize an empty heap
heap = []
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)

# The heap will be a list where the smallest element is at the front
print(heap)  # Output: [1, 3, 2]
```

### Siftup
Given an integer array A, convert A into a minHeap.

```py
# Time: O(nlogn)
# 1. n: iterate over the integer array.
# 2. logn: for every element, it at most need to swap logn times.

class Solution:
    # @param A: An integer array
    # @return: void
    def siftup(self, A, k):
        while k != 0:
            parent = (k - 1) // 2
            if A[k] > A[parent]:
                break
            A[k], A[parent] = A[parent], A[k]
            k = parent
            
    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)
```

### Siftdown
Using the same problem from above: given an integer array A, convert A into a minHeap. Using siftdown to reduce the time complexity down to O(n).

```py
class Solution:
    # @param A: Given an integer array
    # @return: void

    # Instead of looking for the parent of every element from list A, start from a parent of the leaf children.    
    def heapify(self, A):
        for i in range((len(A) - 1) // 2, -1, -1):
            self.siftdown(i, A)

    def siftdown(self, i, A):
        while i * 2 + 1 < len(A):
            child = i * 2 + 1 # index of current left child
            if i * 2 + 1 < len(A) and A[child] > A[k * 2 + 2]:
                child = k * 2 + 2 # if right child is greater than the left child, choose the right child index 
                if A[child] >= A[i]:
                    break 

            A[child], A[i] = A[i], A[child]. 
```

