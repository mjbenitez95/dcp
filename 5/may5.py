# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer 
# that does not exist in the array. The array can contain duplicates and 
# negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] 
# should give 3.

# You can modify the input array in-place.

def least_missing_positive_integer(arr):
  counter = 1
  tmp = 0
  
  for ind in range(1, len(arr)):
    while arr[ind] == counter:
      tmp = arr[counter]
      arr[counter] = arr[ind]
      arr[ind] = tmp

      counter += 1

  counter = 1
  for ind in range(1, len(arr)):
    if counter != arr[ind]:
      break
    counter += 1

  return counter
    
def main():
  print(least_missing_positive_integer([-1, 1, 3, 2, 1, 4, 6]))
  print(least_missing_positive_integer([-1, 2, 4, 5, 1]))
  print(least_missing_positive_integer([3, 4, -1, 1]))
  print(least_missing_positive_integer([1, 2, 0]))
  print(least_missing_positive_integer([-3, -2, -1]))
  print(least_missing_positive_integer([-3, -2, 1]))

if __name__ == '__main__':
  main()

