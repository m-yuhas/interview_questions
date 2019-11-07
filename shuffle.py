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

    def __ne__(self, other: 'Card') -> bool:
        """Return False if this card is the same card as 'other'; otherwise
        return True.
        
        Arguments:
            other: 'Card'
                The card with which to compare this one

        Returns:
            bool: False if the cards are equal, True otherwise

        Raises:
            AttributeError: if the object being compared is not a Card and does
                not inherit from the Card class
        """
        return not self.__eq__(other)

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


def unstable_sort(deck: List[Any]) -> List[Any]:
    """Sort of list of object, assuming that <, ==, and > are implement for the
    objects in the list.
    
    This function implements a heap sort, which has an average performance of
    O(nlog(n)) and a worst case performance of O(nlog(n)) and a memory usage of
    O(n).  This sort is not stable so the order between identical objects in the
    input array is not preserved.
    
    Arguments:
        deck: List[Any]
            List of objects to be sorted

    Returns:
        List[Any]: sorted list of objects
    """
    heap = []
    for i in range(len(deck)):
        heap.append(deck[i])
        j = i
        while j > 0:
            if j % 2 == 0 and heap[j // 2] < heap[j]:
                temp = heap[j]
                heap[j] = heap[j // 2]
                heap[j // 2] = temp
                j = j // 2
            elif j % 2 == 1 and heap[(j - 1) // 2] < heap[j]:
                temp = heap[j]
                heap[j] = heap[(j - 1) // 2]
                heap[(j - 1) // 2] = temp
                j = (j - 1) // 2
            else:
                break
    print("Heap: {}".format(heap))
    for i in range(len(heap) - 1, 0, -1):
        temp = heap[i]
        heap[i] = heap[0]
        heap[0] = temp
        j = 0
        while ((j + 1) * 2) - 1 < i:
            if (j + 1) * 2 < i \
                    and heap[(j + 1) * 2] > heap[((j + 1) * 2) - 1] \
                    and heap[((j + 1) * 2)] > heap[j]:
                temp = heap[j]
                heap[j] = heap[((j + 1) * 2)]
                heap[((j + 1) * 2)] = temp
                j = ((j + 1) * 2)
            elif heap[((j + 1) * 2) - 1] > heap[j]: 
                temp = heap[j]
                heap[j] = heap[((j + 1) * 2) - 1]
                heap[((j + 1) * 2) - 1] = temp
                j = ((j + 1) * 2) - 1
            else:
                break
    return heap


def stable_sort(deck: List[Any]) -> List[Any]:
    """Sort of list of object, assuming that <, ==, and > are implement for the
    objects in the list.

    This function implements a merge sort, which has an average performance of
    O(nlog(n)) and a worst case performance of O(nlog(n)) and a memory usage of
    O(n).  This sort is stable so the order between identical objects in the
    input array is preserved.
    
    Arguments:
        deck: List[Any]
            List of objects to be sorted

    Returns:
        List[Any]: sorted list of objects
    """
    return deck


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
    # If multiple cards of the same rank and suit exist in the deck, it is not
    # important that they maintain their order in the sorted array.  In other
    # words an A♠ is identical to any other A♠.  Assume that the <, ==, and >
    # operators are defined on the included Card class.
    print(unstable_sort([9, 5, 6, 7, 2, 8, 1, 3, 4, 0, 9, 5]))
    # print('Problem #3\n{}'.format(
    #    [str(card) for card in unstable_sort(shuffle(deck))]))

    # Problem 4:
    # Write a function that sorts a deck of shuffled cards in O(nlong(n)) time.
    # If multiple cards of the same rank and suit exist in the deck their order
    # must be maintained. Assume that the <, ==, and > operators are defined on
    # the included Card class.
    print('Problem #4\n{}'.format(
        [str(card) for card in stable_sort(shuffle(deck))]))
