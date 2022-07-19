# Suppose you have a multiplication table that is N by N. That is, a 2D array
# where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 
# 0-indexed) or i * j (if 1-indexed).
#
# Given integers N and X, write a function that returns the number of times
# X appears as a value in an N by N multiplication table.
#
# For example, given N = 6 and X = 12, you should return 4.

def num_occurences(dimension, value):
    occurences = 0

    for i in range(1, dimension + 1):
        a = value / i
        
        if a.is_integer():
            if a <= dimension:
                occurences += 1
        
    return occurences

def main():
    print(num_occurences(6, 12) == 4)
    print(num_occurences(6, 36) == 1)

if __name__ == "__main__":
    main()