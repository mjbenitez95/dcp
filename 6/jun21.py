# Given a function that generates perfectly random numbers between 1 and k
# (inclusive), where k is an input, write a function that shuffles a deck of
# cards represented as an array using only swaps.
#
# It should run in O(N) time.
#
# Hint: Make sure each one of the 52! permutations of the deck is equally
# likely.

from random import randint

# Fisher-Yates shuffle algorithm
def shuffle(deck):
    num_cards = len(deck)

    for index in range(num_cards - 1, 0, -1):
        new_place = randint(0, index + 1)
        
        # swap places
        tmp = deck[new_place]
        deck[new_place] = deck[index]
        deck[index] = tmp

    return deck

def main():
    deck = [
        "AC", "AS", "AH", "AD",
        "2C", "2S", "2H", "2D",
        "3C", "3S", "3H", "3D",
        "4C", "4S", "4H", "4D",
        "5C", "5S", "5H", "5D",
        "6C", "6S", "6H", "6D",
        "7C", "7S", "7H", "7D",
        "8C", "8S", "8H", "8D",
        "9C", "9S", "9H", "9D",
        "10C", "10S", "10H", "10D",
        "JC", "JS", "JH", "JD",
        "QC", "QS", "QH", "QD",
        "KC", "KS", "KH", "KD",
    ]
    print(shuffle(deck))

if __name__ == "__main__":
    main()