# Lintcode problem 64: https://www.lintcode.com/problem/64/description?fromId=161&_from=collection

# first try:
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    """
 p
              e
    [0, 0, 0, 0, 9, 10, 11, 12, 13]
           p
    [4,5,6,7]
    """
    def mergeSortedArray(self, A, m, B, n):
        if not B:
            return A

        p1, p2 = m - 1, n - 1
        p1_end = m + n - 1

        while p2 >= 0 and p1_end >= p1:
            aPointer = A[p1] if p1 >= 0 else float("-inf")
            if aPointer > B[p2]:
                A[p1_end] = aPointer
                aPointer = 0
                p1 -= 1
                p1_end -= 1
            else:
                A[p1_end] = B[p2]
                p2 -= 1
                p1_end -= 1
        return A

    



