## Description
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.The overall run time complexity should be O(log(m+n)).

[Leetcode problem 4](https://leetcode.com/problems/median-of-two-sorted-arrays/)

```
The definition of the median:

The median here is equivalent to the median in the mathematical definition.
The median is the middle of the sorted array.

If there are n numbers in the array and n is an odd number, 
the median is A[(n−1)/2].
If there are n numbers in the array and n is even, 
the median is A[(n−1)/2]+A[(n−1)/2+1])/2.

For example, the median of the array A=[1,2,3] is 2, 
and the median of the array A=[1,19] is 10.
```

Given a list of A and B, A = [1, 2, 3, 4, 5, 6, 7, 8], B = [1, 2, 3, 4, 5]

we don't need to use binary search on both lists. 

- count the total elements stored in list A and list B, as it would be the length of the new list if list A and list B are combined. In the above example, if the new list is created, the length of the new list would be 13.
```py
total_len = len(A) + len(B) # 13
mid_if_new_list_is_formed = total_len // 2 # 6
``` 

- choose the shorter list B to run a binary search operation.
```py
# use two pointers on list B, L stands for left pointer and R stands for right pointer.
mid_pointerB = (L + R) // 2 # 2 
# B[mid_pointerB] == 3

num_of_elementments_on_the_left_of_mid_pointerB_inclusive = mid_pointerB + 1 # 3
```

- There is no need to run a separate binary search on list A. The mid_pointerA could be calculated. Note: the mid pointer doesn't have to be pointing at the exact middle element of A list. 
```py
mid_pointerA = mid_if_new_list_is_formed - num_of_elementments_on_the_left_of_mid_pointerB_inclusive - 1
# evaluate to 2, need to -1 because list is 0 indexed 
```

### Odd number

```py
#          P1
A = [1, 2, 3, 4, 5, 6, 7, 8]
#          P2
B = [1, 2, 3, 4, 5]
```

- We have the following two known condition: B[P2] <= B[P2 + 1] AND A[P1] <= A[P1 + 1]
- We need to check:
1. if A[P1] <= B[P2 + 1]
2. if B[P2] <= A[P1 + 1] 
- The above example satisfies both conditions, now compare A[P1 + 1] and B[P2 + 1], return the smaller number 
```py
return min(A[P1 + 1], B[P2 + 1]) # 4
```

### Even number

```py
#             P1
A = [1, 2, 3, 4, 5, 6, 7, 8]
#    L P2     R 
B = [1, 2, 3, 4]

total_length == 12 
mid_if_new_list_is_formed = total_length // 2 # 6
P2 = (3 + 0) // 2 # 1 
# P1 = mid pointer of the new list - the number of elements on the left, inclusive of P2, in the above case, 2 elements. 
number_of_elements_P1_should_reference = mid_if_new_list_is_formed - (P2 + 1) # 4
P1 = number_of_elements_P1_should_reference - 1 # 3
```
- We still have the following two known condition: B[P2] <= B[P2 + 1] AND A[P1] <= A[P1 + 1]
- We need to check:
1. if 4 <= 3 
2. if 2 <= 5 

condition 1 is false but not condition 2. 
- What to do? 
1. move the left pointer of list B to P2 + 1.
```py
#          L  R 
B = [1, 2, 3, 4] 
P2 = (3 + 2) // 2 # 2 
P1 = 6 - (2 + 1) - 1
```

```py
#             P1
A = [1, 2, 3, 4, 5, 6, 7, 8]

#          P2 
#          L  R 
B = [1, 2, 3, 4]
```
- We need to check:
1. if 4 <= 4 
2. if 3 <= 5 

```py
# compare A[P1] and A[P2], choose the larger one
# compare A[P1 + 1] and A[P2 + 1], choose the smaller one 
return (max(A[P1], B[P2]) + min(A[P1 + 1], B[P2 + 1])) / 2
```


