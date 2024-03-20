Question: Imagine an array of numbers where every number occurs twice. However, one number appears only once. How would you find this number in O (log n) time?

Since the problem asks for a O(logN) solution, I have to assume that the numbers are already sorted, meaning the same number are adjacent to each other, the value of the numbers shouldn't matter, and they expect us to use Binary Search.

First, we should analyze the pattern of a regular number array without a single disrupter. 
Index: 0 1 2 3 4. 5 6. 7. 8. 9 
Array:[1, 1, 2, 2, 4, 4, 5, 5, 6, 6]

notice the odd indexes are always referencing the second of the reoccurring numbers and the even indexes reference the first of reoccurring numbers.

Now, given a number array with a single disrupter: Index: 0 1 2 3 4 5 6 7 8 9 10 Array:[1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

Here is python initial pseudo code:

```py
n = len(Array)
left, right = 0, n - 1
while left <= right:
  mid = (left + right) // 2
  # even index, check the number to the right, if it's the same number, it means Array[mid:] is a regular number sub-array without the disrupter, therefore, the disrupter should be at Array[:mid]
  if mid % 2 == 0:
    if Array[mid] == Array[mid + 1]:
      right = mid - 1
    else:
      left = mid + 1
  # odd index, check the number to the left, if it's the same number, explore right half of sub-array, else the left half
  else:
    if Array[mid] == Array[mid - 1]:
      left = mid + 1
    else:
      right = mid - 1
Break out of while loop:
return Array[left]
```