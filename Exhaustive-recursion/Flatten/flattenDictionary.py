"""
Pramp problem: https://www.pramp.com/challenge/AMypWAprdmUlaP2gPVLZ
"""
"""
Edge case:
  if the dictionary is empty:
    return {} 
  create a dictionary, output.
  create a helper function, "", output, dictionary 
  return output 

helper function:
  iterate over dictionary by keys, with k:
    past_key = past_key+"."+key if past_key is True else key
    base case:
      if type of dictionary[key] is not dictionary:
          output[past_key] = dictionary[k]
        return 
        
    call helper function(past_key, k, output, dictionary[k])

output = {"key1": "1", }
"""

def flatten_dictionary(dictionary):
  if not dictionary:
    return {}
  output = {}
  _flatten("", output, dictionary)
  return output 

def _flatten(past_key, output, dictionary):
  for k in dictionary:
    if past_key and k:
      key = past_key + "." + k
    elif past_key and not k:
      key = past_key 
    elif not past_key and k:
      key = k 
    elif not past_key and not k:
      key = ""
    if type(dictionary[k]) != dict:
      output[key] = dictionary[k]
    else:
      _flatten(key, output, dictionary[k])
