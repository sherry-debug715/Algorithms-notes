# this solution beats 99.8% submissions

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    """
    The tricky part of the problem is how to handle "*"
    When encounter a "*" in p, use star_pointer to reference the position of the "*" and tempStr_pointer for the current index of s, keep p_pointer at star_pointer + 1. 
    For example:
    Input:
       s
    "cbbba"
       p
    "c?*a"

    starIdx, tempStr_pointer = 2, 2
    now increment p by one, but not s, to see if the next letter match, this is as if we are treating the "*" as an empty string. 
       s
    "cbbba"
        p
    "c?*a"
    since "b" != "a", and "*" could also represent "b". We can check if we are in a "*" situation by checking if starIdx is not -1. 
    starIdx, tempStr_pointer = 2, 3
        s
    "cbbba"
        p
    "c?*a"
    at last, "*" represents "bb"
    starIdx, tempStr_pointer = 2, 4
         s
    "cbbba"
        p
    "c?*a"
    """
    def is_match(self, s: str, p: str) -> bool:
        str_pointer, p_pointer = 0, 0
        starIdx, tempStr_pointer = -1, -1 

        while str_pointer < len(s):
            if p_pointer < len(p) and (s[str_pointer] == p[p_pointer] or p[p_pointer] == "?"):
                str_pointer += 1
                p_pointer += 1
            elif p_pointer < len(p) and p[p_pointer] == "*":
                starIdx = p_pointer
                tempStr_pointer = str_pointer
                p_pointer += 1
            elif starIdx != -1:
                p_pointer = starIdx + 1
                tempStr_pointer += 1
                str_pointer = tempStr_pointer
            else:
                return False
        
        while p_pointer < len(p):
            if p[p_pointer] != "*":
                return False 
            p_pointer += 1
        return True
