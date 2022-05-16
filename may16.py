import random

from numpy import average

# Given a stream of elements too large to store in memory, pick a random 
# element from the stream with uniform probability.

def pick(big_stream):
    picked_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            picked_element = e
        elif random.randint(1, i + 1) == 1:
            picked_element = e
    return picked_element

if __name__ == '__main__':
  runs = 100000
  nums = list(range(1, 50 + 1))
  picks = [0] * len(nums)

  for i in range(runs):
    picked_number = pick(nums) - 1
    picks[picked_number] = picks[picked_number] + 1

  avg = round(average(picks))
  deviations = []
  for i in picks:
    deviations.append(abs(avg - i))
  
  max_percent_deviation = (max(deviations) / runs) * 100
  print(max_percent_deviation, deviations)
