# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 
# 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not
#  allowed.

from math import floor


MAPPINGS = {
  '1': 'a',
  '2': 'b',
  '3': 'c',
  '4': 'd',
  '5': 'e',
  '6': 'f',
  '7': 'g',
  '8': 'h',
  '9': 'i',
  '10': 'j',
  '11': 'k',
  '12': 'l',
  '13': 'm',
  '14': 'n',
  '15': 'o',
  '16': 'p',
  '17': 'q',
  '18': 'r',
  '19': 's',
  '20': 't',
  '21': 'u',
  '22': 'v',
  '23': 'w',
  '24': 'x',
  '25': 'y',
  '26': 'z'
}

def is_true(var):
  return var == True

def ways_to_decode(num_str):
  num_ways = 0

  
  decodable = list(filter(lambda x: x == True, 
  [
    num_str[i] in MAPPINGS,
    num_str[i+1] in MAPPINGS,
    (num_str[i] + num_str[i + 1]) in MAPPINGS
  ]))

  num_ways += len(decodable)

  return num_ways


def main():
  print(ways_to_decode("111"))
  print(ways_to_decode("12321"))
  return

if __name__ == '__main__':
  main()
