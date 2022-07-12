# Using a function rand5() that returns an integer from 1 to 5 (inclusive) 
# with uniform probability, implement a function rand7() that returns an
# integer from 1 to 7 (inclusive).

from random import randint


def rand5():
  return randint(1,5)

def rand7():
  num = rand5() + rand5() + rand5() + rand5() + rand5() + rand5() + rand5()
  return num % 7

def main():
  nums = [0] * 7
  for _ in range(1, 1000000):
    nums[rand7() - 1] += 1

  print(nums)

if __name__ == "__main__":
  main()
