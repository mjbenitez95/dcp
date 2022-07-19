# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first 
# and last element of that pair. For example, car(cons(3, 4)) returns 3, and 
# cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
# def cons(a, b):
#    def pair(f):
#        return f(a, b)
#    return pair
#
# Implement car and cdr.

def cons(a, b):
  def pair(f):
    return f(a, b)
  return pair

def car(pair):
  def first_element(a,_):
    return a
  return pair(first_element)

def cdr(pair):
  def second_element(_,b):
    return b
  return pair(second_element)

print(car(cons('a','b')))
print(cdr(cons('a','b')))
