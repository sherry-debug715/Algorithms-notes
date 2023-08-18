class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s: str) -> bool:
        # Write your code here

        # use two pointers
        # build a helper function that checks if a given string from given index1 to given index2 is a 
            # valid palindrome, the function should return a boolean.
        # while pointer1 < pointer2
            # when s[pointer1] != s[pointer2] 
                # there is only one chance of been wrong 
                # this is a critical point here, choose right side, or choose left side.
                # ref1 = pass pointer1 + 1 to helper function 
                # ref2 = pass pointer 2 -= 1 to helper function 
                # return ref1 or ref2
        
        # always consider edge case
        if s is None:
            return False

        pointer1, pointer2 = 0, len(s) - 1  

        while pointer1 < pointer2:
            if s[pointer1] != s[pointer2]:
                choose_left = self._valid_palindrome(pointer1 + 1, pointer2, s) 
                choose_right = self._valid_palindrome(pointer1, pointer2 - 1, s)
                return choose_left or choose_right
                
            pointer1 += 1 
            pointer2 -= 1 
        
        return True 
    
    def _valid_palindrome(self, pointer1, pointer2, s):
        while pointer1 < pointer2:
            if s[pointer1] != s[pointer2]:
                return False 
            
            pointer1 += 1
            pointer2 -= 1 

        return True