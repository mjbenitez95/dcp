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
  runs = 350000
  for _ in range(1, runs):
    nums[rand7() - 1] += 1

  success = True
  for num in nums:
    # accept 1.2 % deviation
    if (num / (runs / 7)) > 1.2:
      success = False

  print(success)

if __name__ == "__main__":
  main()
