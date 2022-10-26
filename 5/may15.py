# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using
# a Monte Carlo method.
#
# Hint: The basic equation of a circle is x^2 + y^2 = r^2.

from math import sqrt
import random

RUNS = 1000000000

def distance(point_a, point_b):
  return sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

def main():
  points_inside_circle = 0
  center_of_circle = [0.5, 0.5]

  for _ in range(0, RUNS + 1):
    random_point = [random.random(), random.random()]
    if distance(random_point, center_of_circle) <= 0.5:
      points_inside_circle = points_inside_circle + 1

  ratio_of_points = points_inside_circle / RUNS
  approximated_pi = round(ratio_of_points * 4, 10)
  print("Pi approximated to:", approximated_pi)

  return

if __name__ == '__main__':
  main()
