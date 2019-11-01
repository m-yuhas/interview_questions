#!/usr/bin/env python
from itertools import product

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return 'CARD\nsuit: {}\nrank: {}\n'.format(self.suit, self.rank)

if __name__ == "__main__":
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    deck = [Card(combo[0], combo[1]) for combo in product(*[suits, ranks])]
    for i in deck:
        print(i)
        
    # Problem 1:
    # Write a function that shuffles a deck of cards in O(n) time.
    
    # Problem 2:
    # How good is the O(n) shuffle function, i.e. is every card equally likely
    # to end up in each final position?
    
    # Problem 3:
    # Write a shuffle function that minimizes the difference between the
    # probabilities of a card ending up in any given position in the shuffled
    # deck.
    
    # Problem 4:
    # Simulate the new shuffle function to show its performance.
        
