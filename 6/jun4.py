# Given a string, find the palindrome that can be made by inserting the fewest
# number of characters as possible anywhere in the word. If there is more than
# one palindrome of minimum length that can be made, return the
# lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we
# can add three letters to it (which is the smallest amount to make a 
# palindrome).There are seven other palindromes that can be made from "race"
# by adding three letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".

def isPalindrome(s):
    return s == s[::-1]

def fewestPalindrome(s):
    count = 1
    
    while(True):
        beginning = s[0-count:][::-1] + s
        end = s + s[:count][::-1]
        
        if (isPalindrome(beginning) and isPalindrome(end)):
            if beginning < end:
                return beginning
            return end
            
        if (isPalindrome(beginning)):
            return beginning
            
        if (isPalindrome(end)):
            return end
        
        count += 1
        
def main():
    print(fewestPalindrome("race") == "ecarace")
    print(fewestPalindrome("google") == "elgoogle")
    print(fewestPalindrome("matthew") == "matthewehttam")
        
if __name__ == '__main__':
    main()
