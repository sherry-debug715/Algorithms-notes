# Pramp problem: https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5Lg1

"""
Initialize two pointers, pointerA, pointerB, set them at 0, 0
while pointerA < length of slotsA and pointerB < length of slotsB:
  [epochA1, epochA2] = slotsA[pointerA]
  [epochB1, epochB2] = slotsB[pointerB] 
  Initialize a number, diff, set it to:
    diff = min(epochB2, epochA2) - max(epochA1, epochB1)
    if diff >= dur:
      return a list of max(epochA1, epochB1), max(epochA1, epochB1) + dur 
    pointerA += 1
    pointerB += 1 
  
  return []
"""

def meeting_planner(slotsA, slotsB, dur):
  pointerA, pointerB = 0, 0 
  
  while pointerA < len(slotsA) and pointerB < len(slotsB):
    [epochA1, epochA2] = slotsA[pointerA]
    [epochB1, epochB2] = slotsB[pointerB] 
    diff = min(epochB2, epochA2) - max(epochA1, epochB1)
    if diff >= dur:
      start = max(epochA1, epochB1)
      return [start, start + dur]
    
    if epochB2 < epochA2:
      pointerB += 1
    else:
      pointerA += 1
  
  return []


