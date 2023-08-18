class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        if not target or not source: # not source added latter
            return 0

        target_length = len(target)
        
        for idx in range(len(source) - target_length + 1):
            if source[idx] != target[0]:
                continue
            if source[idx:idx+target_length] == target:
                return idx

        return -1
