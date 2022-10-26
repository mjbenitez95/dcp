import random

# Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.
# The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.
# The second game: same, except that the stopping condition is a five followed by a five.
# Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

NUM_RUNS = 1000000

def main():
  total_cost = 0

  for _ in range(0, NUM_RUNS):
    cost = 0
    while True:
      cost += 1
      if random.randint(1, 6) != 5:
        next
      cost += 1
      if random.randint(1, 6) == 6:
        break
    
    total_cost = total_cost + cost
    
  total_cost_b = 0

  for _ in range(0, NUM_RUNS):
    cost_b = 0
    while True:
      cost_b += 1
      if random.randint(1, 6) != 5:
        next
      cost_b += 1
      if random.randint(1, 6) == 5:
        break
    
    total_cost_b = total_cost_b + cost_b

  print(total_cost / NUM_RUNS)
  print(total_cost_b / NUM_RUNS)

if __name__ == "__main__":
  main()

