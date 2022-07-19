# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original
# array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
# be [2, 3, 6].

# Follow-up: what if you can’t use division?

from functools import reduce

def generate_products(nums):
  products = [0] * len(nums)
  total = reduce((lambda x, y: x * y), nums)
  for idx, x in enumerate(nums):
    products[idx] = round(total / x)

  return products

def main():
  print(generate_products([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
  print(generate_products([3, 2, 1]) == [2, 3, 6])

if __name__ == "__main__":
  main()
