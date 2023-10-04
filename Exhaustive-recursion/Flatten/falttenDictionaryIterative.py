"""
Pramp problem: https://www.pramp.com/challenge/AMypWAprdmUlaP2gPVLZ
"""

def flatten_dictionary(dictionary):
  if not dictionary:
    return {}
  
  output = {}
  stack = [("", dictionary)]
  
  while stack:
    prefix, dic = stack.pop()
    for key, val in dic.items():
      if isinstance(val, dict):
        if not prefix:
          stack.append((key, val))
        else:
          new_key = prefix + "." + key
          stack.append((new_key, val))
      else:
        if not prefix:
          output[key] = val
        elif prefix and key:
          new_key = prefix + "." + key
          output[new_key] = val 
        elif prefix and not key:
          output[prefix] = val
  return output 
        
        

