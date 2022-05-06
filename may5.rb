# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer 
# that does not exist in the array. The array can contain duplicates and 
# negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] 
# should give 3.

# You can modify the input array in-place.

def least_missing_positive_integer(arr)
  i = 0

  while i < arr.length
    if (arr[i] > 0 && arr[i] <= arr.length && arr[arr[i] - 1] != arr[i])
      puts "a, #{i}"
      tmp = arr[i]
      arr[i] = arr[arr[i] - 1]
      arr[arr[i] - 1] = tmp
    else
      puts 'b'
      i = i+1
    end
  end

  for a in 0..arr.length
    if arr[a] != a+1
      return a+1
    end
  end

  return n + 1
end

puts least_missing_positive_integer([-1,2,4,5,1])
