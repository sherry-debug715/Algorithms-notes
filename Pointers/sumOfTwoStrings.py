# Lintcode problem 1343: https://www.lintcode.com/problem/1343/?fromId=161&_from=collection

class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return the sum of two strings
          p
    A = "99"
           p
    B = "111"
    1,10,10
    """
    def sumof_two_strings(self, a: str, b: str) -> str:
        if not a and not b:
            return ""
        
        output = ""
        p1, p2 = len(a) - 1, len(b) - 1

        while p1 >= 0 or p2 >= 0:
            num1 = int(a[p1]) if p1 >= 0 else 0
            num2 = int(b[p2]) if p2 >= 0 else 0
            cur_sum = num1 + num2
            output = str(cur_sum) + output
            p1 -= 1
            p2 -= 1
        
        return output