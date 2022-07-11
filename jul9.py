# Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.
 
def max_product_of_three(nums):
  nums.sort()
  with_negatives = nums[0] * nums[1] * nums[-1]
  only_positives = nums[-1] * nums[-2] * nums[-3]
  return max(with_negatives, only_positives)

def main():
  print(max_product_of_three([1, 5, 7, 2, 3]))
  print(max_product_of_three([-10, -10, 5, 2]))
  print(max_product_of_three([7, 8, 2, 15, 0]))
  print(max_product_of_three([-50, 35, 10, 20, 0]))

if __name__ == "__main__":
  main()

