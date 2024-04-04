def decodeVariations(S):
  """
  @param S: str
  @return: int
  """ 
  def _decodeVariations(index, memo):
    if index == len(S):
      return 1
    
    if index in memo:
      return memo[index]
    
    if S[index] == "0":
      return 0 
    count = _decodeVariations(index + 1, memo) 
    if index < len(S) - 1 and int(S[index:index + 2]) <= 26:
      count += _decodeVariations(index + 2, memo) # F ...
        
    memo[index] = count
    
    return count
  
  return _decodeVariations(0, {})
 

  

