#You are given an N by M 2D matrix of lowercase letters. Determine the minimum
# number of columns that can be removed to ensure that each row is ordered
# from top to bottom lexicographically. That is, the letter at each column is
# lexicographically later as you go down each row. It does not matter whether
# each row itself is ordered lexicographically.

def non_lexicographical_columns(matrix):
    to_remove = 0
    top_row = matrix[0]
    cur_letter = ''

    for index, letter in enumerate(top_row):
        cur_letter = letter 
        for lower_row in matrix[1:]: # disregard top row

            next_letter = lower_row[index]
            
            if ord(next_letter) < ord(cur_letter):
                to_remove += 1
                break

            cur_letter = next_letter

    return to_remove

def main():
    a = [
        ['c', 'b', 'a'],
        ['d', 'a', 'f'],
        ['g', 'h', 'i']
    ]
    
    b = [
        ['a', 'b', 'c', 'd', 'e', 'f']
    ]
    
    c = [
        ['z', 'y', 'x'],
        ['w', 'v', 'u'],
        ['t', 's', 'r']
    ]
    
    print(non_lexicographical_columns(a) == 1)
    print(non_lexicographical_columns(b) == 0)
    print(non_lexicographical_columns(c) == 3)
    pass

if __name__ == "__main__":
    main()