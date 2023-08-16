class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        # edge cases:
        # 1. when target string is empty
        # 2. when target length is greater than length of source

        # use 2 pointers, one pointer to point at souce string, and one at 
        # target string. 
        # once source[pointer1] == target[pointer2], use a variable firstIndex to 
        # reference pointer1, and while values of both pointers equal, 
        # increment both pointers. 
        # break out of the while loop, if pointer2 == len(target), return firstIndex.
        # else set pointer2 to 0. 
        # when pointer1 == len(source), return -1   

        if not target or not source: # not source added latter
            return 0
        
        pointer1, pointer2 = 0, 0
        return_index = -1

        if len(target) > len(source):
            return return_index

        while pointer1 <= len(source) - len(target):
            if source[pointer1] != target[pointer2]:
                pointer1 += 1
                continue
            return_index = pointer1
            while pointer2 < len(target) and source[pointer1] == target[pointer2]:
                pointer1 += 1
                pointer2 += 1
            
            if pointer2 == len(target):
                return return_index
            
            pointer2 = 0
            # it's very important to set pointer1 back to the next element of where we last found a matching value.
            # for example:
            #      |
            # mississippi
            #     |
            # issip
            # first, we will find a matching value at index 1, but break out of while loop when pointer1 is at index 5, if we don't set pointer1 back at index 2, we would have missed index 4.
            pointer1 = return_index + 1
            return_index = -1
        
        return return_index

