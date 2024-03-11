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

        # find the last number in A that's not 0
        p1, p2 = 0, len(B) - 1
        while A[p1] != 0:
            p1 += 1

        p1 = p1 - 1 if p1 > 0 else 0
        p1_end = len(A) - 1

        while p2 >= 0 and p1 >= 0 and p1_end >= p1:
            if A[p1] > B[p2]:
                A[p1_end] = A[p1]
                A[p1] = 0
                p1 -= 1
                p1_end -= 1
            else:
                A[p1_end] = B[p2]
                p2 -= 1
                p1_end -= 1
        if p2 >= 0:
            for i in range(p2, -1, -1):
                A[p1_end] = B[p2]
                p1_end -= 1
                p2 -= 1
        
        return A

    



