#!/usr/bin/env python


from itertools import product
from random import randint
from typing import List


class Card(object):
    """A playing card.
    
    Arguments:
        suit: str
            The suit of the card
        rank: str
            The rank of the card
    """

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        """Return a string representing this card.

        Returns:
            str: a string representing this card.
        """
        return '{}{}'.format(self.rank, self.suit)


def fast_shuffle(deck: List[Card]) -> List[Card]:
    """Shuffle a deck of cards in O(n) time.
    
    Arguments:
        deck List[Card]
            The deck of cards to shuffle

    Returns:
        List[Card]: the shuffled deck
    """
    for i in range(len(deck) - 1):
        j = randint(i, len(deck) - 1)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
    return deck
        


if __name__ == '__main__':
    suits = ['♠', '♣', '♡', '♢']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    deck = [Card(combo[0], combo[1]) for combo in product(*[suits, ranks])]
        
    # Problem 1:
    # Write a function that shuffles a deck of cards in O(n) time.
    print('Problem #1\n{}'.format([str(card) for card in fast_shuffle(deck)]))
    
    # Problem 2:
    # How good is the O(n) shuffle function, i.e. is every card equally likely
    # to end up in each final position?
    
    # Problem 3:
    # Write a shuffle function that minimizes the difference between the
    # probabilities of a card ending up in any given position in the shuffled
    # deck.
    
    # Problem 4:
    # Simulate the new shuffle function to show its performance.
        
