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
        
