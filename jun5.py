# Given an array of strictly the characters 'R', 'G', and 'B', segregate the
# values of the array so that all the Rs come first, the Gs come second, and
# the Bs come last. You can only swap elements of the array.
# Do this in linear time and in-place.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
# become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def rgb_sort(letters):
  tmp = ''
  left, right = 0, len(letters) - 1

  # first pass, move all Rs to the left by swapping when right is R and left is not R   
  while True:
    if left >= right:
      break

    if letters[left] != 'R' and letters[right] == 'R':
      tmp = letters[left]
      letters[left] = letters[right]
      letters[right] = tmp
      left += 1
      right -= 1
      continue

    if letters[left] == 'R':
      left += 1 
    
    if letters[right] != 'R':
      right -= 1

  # reset pointers
  left, right = 0, len(letters) - 1 

  # second pass, move all Bs to the right by swapping when left is B and right is not B
  while True:
    if left >= right:
      break

    if letters[left] == 'B' and letters[right] != 'B':
      tmp = letters[left]
      letters[left] = letters[right]
      letters[right] = tmp
      left += 1
      right -= 1
      continue

    if letters[left] != 'B':
      left += 1 
    
    if letters[right] == 'B':
      right -= 1

  return letters

def main():
  print(rgb_sort(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B'])
  print(rgb_sort(['G', 'G', 'G', 'G', 'B', 'R', 'G']) == ['R', 'G', 'G', 'G', 'G', 'G', 'B'])
  print(rgb_sort(['G', 'R', 'R', 'R', 'B']) == ['R', 'R', 'R', 'G', 'B'])

if __name__ == '__main__':
  main()
