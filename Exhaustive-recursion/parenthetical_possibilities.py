# Write a function, parenthetical_possibilities, that takes in a string as an argument. The function should return an array containing all of the strings that could be generated by expanding all parentheses of the string into its possibilities.

# For example, the possibilities for 'x(mn)yz' are 'xmyz', 'xnyz'.

# parenthetical_possibilities('x(mn)yz') # -> 
# [ 'xmyz', 'xnyz' ]

# parenthetical_possibilities("(qr)ab(stu)c") # ->
# [ 'qabsc', 'qabtc', 'qabuc', 'rabsc', 'rabtc', 'rabuc' ]

# def parenthetical_possibilities(s):
#   if len(s) == 0:
#     return ['']
#   (choice, remainder) = explore_potential(s)
#   break_down = parenthetical_possibilities(remainder)
#   #iterate over choice, if choice returns the string inside parentheses, 
#   # choice length >= 1, use for loop to split the stack tree
#   option = []
#   print('choice', choice)
#   print('remainder', remainder)
#   for each_str in choice:
#     print('each_str', each_str)
#     option += [each_str+ele_remainer for ele_remainer in break_down]
#   return option
    
# def explore_potential(s):
#   # return a tuple separating what's in the parentheses and the string after 
#   # the parentheses
#   # return the 1st ele and the remaining string if no parentheses  
#   if s[0] == '(':
#     end = s.index(')')
#     inside = s[1:end]
#     remainder = s[end+1:]
#     return (inside, remainder)
#   else:
#     return (s[0], s[1:])

def parenthetical_possibilities(s):
  if len(s) == 0:
    return ['']
  
  prefix, remainder = parse_str(s)
  suffix = parenthetical_possibilities(remainder)
  
  result = []
  for char in prefix:
    for i in suffix:
      result.append(char+i)
  return result
  

  
def parse_str(s):
  if s[0] == '(':
    end_index = s.index(')')
    # prefix, remainder
    return (s[1:end_index], s[end_index+1:])
  else:
    return (s[0],s[1:])


print(parenthetical_possibilities('x(mn)yz') )
# parenthetical_possibilities('x(mn)yz') 
# print(parenthetical_possibilities('x(mn)yz'))
# print([]+['de'])