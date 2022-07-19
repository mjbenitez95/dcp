# May 2, 2022 [Easy]
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# time complexity is find * n
def list_sum_k(arr, k)  
  arr.each do |num|
    if arr.find { |num2| num + num2 == k } 
      return true
    end
  end

  false
end

# time complexity is that of the sort
def list_sum_k_in_place_compare(arr, k)
  sorted = arr.sort

  lower_index = 0;
  upper_index = sorted.length - 1

  while lower_index < upper_index
    sum = sorted[lower_index] + sorted[upper_index]

    if sum < k
      lower_index += 1
    elsif sum > k 
      upper_index -= 1
    else
      return true
    end
  end

  false
end

test_cases = [
  {arr: [1, 6, 2, 8, 11, 9], target: 14, expected: true},
  {arr: [0, 7, 3, 14, 6, 11], target: 6, expected: true},
  {arr: [-30, -20, -10, 0, 10, 60, 45, 30], target: 50, expected: true},
  {arr: [7, 20, -30, 5, 16, -20], target: -10, expected: true},
  {arr: [1, 2, 3, 4], target: 15, expected: false},
  {arr: [-30, -10, -20, -15], target: 5, expected: false},
  {arr: [-5, -4, -2, 2, 4, 5], target: 5, expected: false},
  {arr: [-5, -4, -2, 2, 4, 5], target: 5, expected: false},
].freeze

test_cases.each do |test| 
  list_sum_success = list_sum_k(test[:arr], test[:target]) == test[:expected]
  in_place_success = list_sum_k_in_place_compare(test[:arr], test[:target]) == test[:expected]

  puts "List Sum Error" if list_sum_success == false
  puts "In Place Error" if in_place_success == false

  puts "Test Case Passed!" if list_sum_success && in_place_success
end
