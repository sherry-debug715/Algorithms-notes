class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        if not target or not source: # not source added latter. 
            return 0

        target_length = len(target)
        
        for idx in range(len(source) - target_length + 1):
            if source[idx] != target[0]:
                continue
            if self.isSameStr(source, idx, target):
                return idx

        return -1

    def isSameStr(self, source, pointer1, target):
        for idx in range(len(target)):
            if source[pointer1] != target[idx]:
                return False
            pointer1 += 1
        
        return True