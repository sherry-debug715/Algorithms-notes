# Lintcode problem 426: https://www.lintcode.com/problem/426/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
             we will sort your return value in output
    """
    # Time: worst case:  
    def restore_ip_addresses(self, s: str) -> List[str]:
        if not s or len(s) > 12:
            return []
        ips = []
        
        def dfs(idx, dots, ip):
            if dots == 4 and idx == len(s):
                ips.append(ip[1:])
                return 

            if dots > 4:
                return 
            for i in range(idx, min(idx + 3, len(s))):
                if int(s[idx: i + 1]) <= 255:
                    dfs(i + 1, dots + 1, ip + "." + s[idx: i + 1])
                if s[idx] == "0":
                    break 
        
        dfs(0, 0, "")
        return ips
        

         