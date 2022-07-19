# Given an array of integers, write a function to determine whether the array
# could become non-decreasing by modifying at most 1 element.
#
# For example, given the array [10, 5, 7], you should return true, since we can
# modify the 10 into a 1 to make the array non-decreasing.
#
# Given the array [10, 5, 1], you should return false, since we can't modify
# any one element to get a non-decreasing array.

def can_be_non_decreasing(arr):
    decreases = 0
    for index, num in enumerate(arr):
        if index == 0:
            continue

        if num < arr[index - 1]:
            decreases += 1
    
    return decreases <= 1

def main():
    print(can_be_non_decreasing([10, 5, 7]) == True)
    print(can_be_non_decreasing([10, 5, 1]) == False)

if __name__ == "__main__":
    main()