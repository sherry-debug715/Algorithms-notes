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

