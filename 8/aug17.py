# Given two strings A and B, return whether or not A can be shifted some number of times to get B.

# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

# O(nlogn), because of the sort
def can_be_shifted(a, b):
  if len(a) != len(b):
    return False

  sorted_a = sorted(a)
  sorted_b = sorted(b)
  
  for index in range(0, len(sorted_a)):
    if sorted_a[index] != sorted_b[index]:
      return False

  return True

# O(n) because the dict insert and lookup is O(1)
def can_be_shifted_linear(a, b):
  if len(a) != len(b):
    return False

  characters = {}

  for character in a:
    if character not in characters:
      characters[character] = 0
    characters[character] += 1

  for character in b:
    if character not in characters:
      return False
    
    characters[character] -= 1
    if characters[character] == 0:
      characters.pop(character)

  return len(characters) == 0

def main():
  print(can_be_shifted("abcde", "cdeab") == True)
  print(can_be_shifted("abcde", "cdea") == False)
  print(can_be_shifted("abcde", "ccccc") == False)  
  print(can_be_shifted_linear("abcde", "cdeab") == True)
  print(can_be_shifted_linear("abcde", "cdea") == False)
  print(can_be_shifted_linear("abcde", "ccccc") == False)

if __name__ == "__main__":
  main()