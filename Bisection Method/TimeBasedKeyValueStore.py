# Leetcode problem 981: https://leetcode.com/problems/time-based-key-value-store/description/

# Time: O(logN), where N is the number of tuples stored in self.time_store[key]
# Space: O(K+V), where K is the number of unique keys, and V is the total number of value-timestamp pairs across all keys.
class TimeMap:

    def __init__(self):
        self.time_store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_store[key] = self.time_store.get(key, [])
        self.time_store[key].append((value, timestamp))
        # print("self.time_store", self.time_store)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_store:
            return ""
        val = self.locate(key, timestamp)
        if val is not None:
            return val 
        return self.find_nearest(key, timestamp)
    
    def locate(self, key, timestamp):
        store = self.time_store[key] 
        left, right = 0, len(store) - 1 
        while left + 1 < right:
            mid = (left + right) // 2
            mid_val, mid_time = store[mid]
            if mid_time == timestamp:
                return mid_val 
            if mid_time > timestamp:
                right = mid 
            else:
                left = mid 
        
        if store[left][1] == timestamp:
            return store[left][0]
        if store[right][1] == timestamp:
            return store[right][0] 
        return None 
    
    def find_nearest(self,key, timestamp):
        store = self.time_store[key] 
        left, right = 0, len(store) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            mid_key, mid_time = store[mid]
            if mid_time >= timestamp:
                right = mid 
            else:
                left = mid

        if store[right][1] < timestamp:
            return store[right][0]
        if store[left][1] < timestamp:
            return store[left][0]
        return ""
                                     

