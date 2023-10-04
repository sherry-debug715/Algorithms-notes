class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        if not nestedList:
            return []
        output = []
        stack = [nestedList]
        while stack:
            cur = stack.pop()
            if isinstance(cur, list):
                for n in reversed(cur):
                    stack.append(n) 
            else:
                output.append(cur)
        return output

    
