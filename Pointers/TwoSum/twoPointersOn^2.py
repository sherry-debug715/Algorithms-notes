class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    # Time O(n^2)
    # Space O(1)
    
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        # use two pointers, pointer1 start from left
        # while pointer1 < len(numbers)
            # pointer2 = pointer1 + 1
            # while pointer2 < len(numbers)
                # if numbers[pointer1] + numbers[pointer2] == target:
                    # return a list of pointer1 and pointer2 
                # increment pointer2 
            # increment pointer1 

        pointer1 = 0 

        while pointer1 < len(numbers):
            pointer2 = pointer1 + 1
            while pointer2 < len(numbers):
                two_sum = numbers[pointer1] + numbers[pointer2]
                if two_sum == target:
                    return [pointer1, pointer2] 
                pointer2 += 1
            pointer1 += 1