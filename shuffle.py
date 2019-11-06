#!/usr/bin/env python


from itertools import product
from random import randint
from sys import modules
from typing import Any, Callable, List


try:
    from matplotlib import pyplot
except:
    pass


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

    def __eq__(self, other: 'Card') -> bool:
        """Return True if this card is the same card as 'other'; otherwise
        return False.
        
        Arguments:
            other: 'Card'
                The card with which to compare this one

        Returns:
            bool: True if the cards are equal, False otherwise

        Raises:
            AttributeError: if the object being compared is not a Card and does
                not inherit from the Card class
        """
        if self.suit == other.suite and self.rank == other.rank:
            return True
        else:
            return False

    def __hash__(self) -> int:
        """Return the hash of this card such that two cards with the same
        attributes have the same hash.

        Returns:
            int: the hash of this card
        """
        return hash((self.suit, self.rank))

    def __str__(self) -> str:
        """Return a string representing this card.

        Returns:
            str: a string representing this card.
        """
        return '{}{}'.format(self.rank, self.suit)


def shuffle(deck: List[Any]) -> List[Any]:
    """Shuffle a list of objects in O(n) time.
    
    Arguments:
        deck List[Any]
            The list of objects to shuffle

    Returns:
        List[Any]: the shuffled list
    """
    for i in range(len(deck) - 1):
        j = randint(i, len(deck) - 1)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
    return deck


def get_order_bias(shuffle_algorithm: Callable[[List[Any]], List[Any]],
                   deck_size: int,
                   iterations: int) -> List[List[float]]:
    """Find the order bias for any given shuffle algorithm.
    
    Arguments:
        shuffle_algorithm: Callable[List[Any], List[Any]]
            Shuffle function that takes a list of objects and returns the
            shuffled list
        deck: int
            The size of the deck to use when analyzing the order bias
        iterations: int
            Number of shuffles to simulate

    Returns:
        List[List[float]]: a 2-dimensional array of floats where List(x,y) is
            the probability of the object at position x in the input deck ending
            up at position y in the output deck
    """
    bias_matrix = [[0 for col in range(deck_size)] for row in range(deck_size)]
    for i in range(iterations):
        shuffled_deck = shuffle_algorithm([i for i in range(deck_size)])
        for i in range(deck_size):
            bias_matrix[i][shuffled_deck[i]] += 1
    for (x, y) in [(x, y) for x in range(deck_size) for y in range(deck_size)]:
        bias_matrix[x][y] = bias_matrix[x][y] / float(deck_size * iterations)
    return bias_matrix
    


if __name__ == '__main__':
    suits = ['♠', '♣', '♡', '♢']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    deck = [Card(combo[0], combo[1]) for combo in product(*[suits, ranks])]
        
    # Problem 1:
    # Write a function that shuffles a deck of cards in O(n) time.
    print('Problem #1\n{}'.format([str(card) for card in shuffle(deck)]))
    
    # Problem 2:
    # How good is the shuffle function, i.e. is every card equally likely
    # to end up in each final position?
    bias_matrix = get_order_bias(shuffle, 52, int(1e3))
    print('Problem #2\n{}'.format(bias_matrix))
    if 'matplotlib.pyplot' in modules:
        pyplot.imshow(bias_matrix)
        pyplot.title('Bias Matrix for Shuffle Algorithm with a Deck Size of 52')
        pyplot.show()
    
    # Problem 3:
    # Write a function that sorts a deck of shuffled cards in O(nlog(n)) time.
    # (Assume that the <, ==, and > operators are defined on the included Card
    # class.)
    
    # Problem 4:
    # Simulate the performance of the sorting algorithm for decks from size 0 to
    # 1000.
        
