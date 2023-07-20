* The binary heap data structure is __an array object__ that we can view as a nearly complete binary tree.

* Each node of the tree corresponds to an element from an array.

* Computation, given an index i from the heap where i is not the root node of the heap binary tree, or i != 0:

    * find parents: (i - 1) // 2
    * find left child: 2 * i + 1
    * find right child: 2 * i + 2

* There are __two__ types of binary heap, __min-heaps__ and __max-heaps__.

* max-heaps: Array[parent[i]] >= Array[i].
    * Meaning, the value of a node is at most the value of its parent, thus, the node with the largest value is stored at the root.

* min-heaps: Array[parent[i]] <= Array[i]