class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s: str) -> bool:
        # Write your code here
        # step 1: create a helper function that checks if s could be a valid palindrome by returning 
            # a tuple, using two pointers.
        # if step1 proves that s is not a valid palindrome, create a helper function that checks 
            # if the substring within the given two indexes is a valid palindrome. There are two possibilities
                # 1) increment left pointer by one 
                # 2) decrement right pointer by one 
            # return case 1) or case 2) 
        
        if s is None:
            return False

        left, right = self.if_valid_palindrome(0, len(s) - 1, s)

        # if s is a valid palindrome, left should be greater than right 
        if left >= right: 
            return True 

        return self._valid_palindrome(left + 1, right, s) or self._valid_palindrome(left, right - 1, s)

    def if_valid_palindrome(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return left, right 
            
            left += 1 
            right -= 1 

        return left, right 
        
    def _valid_palindrome(self, left, right, s):
        new_left, new_right = self.if_valid_palindrome(left, right, s)

        return new_left >= new_right
