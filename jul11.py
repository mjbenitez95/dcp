import random

# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with
# uniform probability, implement a function rand5() that returns an integer 
# from 1 to 5 (inclusive).

def rand7():
  return random.randint(1,7)

def rand5():
  random_number = rand7()
  while random_number > 5:
    random_number = rand7()

  return random_number

def main():
  nums = [0] * 5
  for i in range(1, 1000000):
    nums[rand5() - 1] += 1

  print(nums)

if __name__ == "__main__":
  main()

