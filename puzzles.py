#!/usr/bin/env python


from itertools import combinations, combinations_with_replacement
from random import uniform
from statistics import mean
from typing import List, Tuple, Union


def six_digit_perfect_square() -> Union[int, None]:
    """Find a six digit perfect square whose three most significant digits in
    base 10 taken as a number are one more than the three least significant
    digits taken as a number.

    Returns:
        The perfect square satisfying the above conditions if found, otherwise
        None.
    """
    for i in range(300, 1000):
        j = i * i
        lsd = j % 1000
        msd = (j - lsd) // 1000
        if msd == lsd - 1:
            return j


def stamp_values(n: int, m: int) -> Tuple[int, List[int]]:
    """Find the maximum postage value and the n values of the stamps required to
    reach it given the following constraints:
    1. There are n stamps with unique values
    2. When posting a letter a maximum of m stamps may be used
    3. The maximum postage value is the maximum value that can be posted with m
    stamps with every lesser integer postage value able to be posted also using
    a maximum of m stamps.
    
    Arguments:
        n: int
            The number of unique stamp values in circulation.
        m: int
            The maximum number of stamps allowed to post a letter.

    Returns:
        Tuple[int, List[int]: The first index of the tuple is the maximum
            postage value.  The second index is a list of the stamps required to
            attain that value.
    """
    max_value = n
    last_match = []
    while True:
        current_match = None
        combos = combinations([i for i in range(1, max_value + 1)], n)
        for stamp_values in combos:
            sums = [0] * (max_value + 1)
            for i in range(m + 1):
                for c in combinations_with_replacement(stamp_values, i):
                    if sum(c) < len(sums):
                        sums[sum(c)] += 1
            try:
                sums[1:].index(0)
            except ValueError as e:
                current_match = stamp_values
                break
        if not current_match:
            return max_value - 1, last_match
        last_match = current_match
        max_value += 1


def shortest_name(names: List[str]) -> Union[str, None]:
    """Find the shortest name in a list of names that shares at least one
    character with every other name in the list.  For example in the list:
    ['add', 'dog', 'tree', 'house', 'gave'], 'gave' is the word that satisfies
    the above requirement.

    Arguments:
        names: List[str]
            List of names to search.

    Returns:
        Union[str, None]: the shortest name that shares a letter in common with
            every other name or None if no such name exists.
    """
    return_list = []
    for current_name in names:
        candidate = True
        for compare_name in names:
            shares_letter = False
            for letter in current_name.replace(' ', ''):
                if letter in compare_name.replace(' ', ''):
                    shares_letter = True
                    break
            if shares_letter == False:
                candidate = False
                break
        if candidate != False:
            return_list.append(current_name)
    if len(return_list) == 0:
        return None
    smallest_name = return_list[0]
    for name in return_list:
        if len(name) < len(smallest_name):
            smallest_name = name
    return smallest_name


def probabilities(n: int, iterations: int) -> float:
    """Find the expected value of the distance the hiker has to walk around the
    circumference of the crater assuming that n re-supply stations have been
    dropped in random locations and the hiker chooses to set off in a random
    direction at the start of the journey.  Simulate this scenario 'iterations'
    number of times to find the expected value.

    Arguments:
        n: int
            Number of re-supply stations dropped on the circumference of the
            crater.
        iterations: int
            The number of iterations to run this simulation.

    Returns:
        float: the expected distance the hiker has to walk to encounter the
            first re-supply station as a percentage of the circumference of the
            crater.
    """
    distances = []
    for i in range(iterations):
        stations = [uniform(0,1) for j in range(n)]
        distances.append(min(stations))
    return mean(distances)


if __name__ == '__main__':
    # Problem 1:
    # Find a six digit number (base 10) that is a perfect square and whose
    # leading three digits taken as a three digit number are one less than the
    # least significant three digits taken a three digit number.
    print('Problem #1\n{}'.format(six_digit_perfect_square()))
    
    # Problem 2:
    # Suppose there are four possible integer values for postage stamps, and
    # each letter or package can receive at maximum, three stamps.  What should
    # the values of the four stamps be so that all postage values from one to
    # some maximum value can be posted with three or fewer stamps.
    max_value, stamp_values = stamp_values(4, 3)
    print('Problem #2:\nMaximum Postage:{}\nStamp Values:{}'.format(
        max_value, stamp_values))

    # Problem 3:
    # Find the shortest name of a US state that has a letter in common with
    # every other state name. 
    states = ['ALABAMA', 'ALASKA', 'ARIZONA', 'CALIFORNIA', 'COLORADO',
              'CONNECTICUT', 'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII',
              'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY',
              'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN',
              'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA',
              'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK',
              'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
              'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
              'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
              'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']
    print('Problem #3:\n{}'.format(shortest_name(states)))

    # Problem 4:
    # Suppose that two re-supply stations are dropped from an aircraft at two
    # random locations on the circumference of a crater.  A hiker approaches the
    # edge of the crater and randomly decides to walk clockwise or
    # counter-clockwise around the equator.  Find the expected value of the
    # distance that the hiker will walk (in terms of the circumference of the
    # crater) before encountering a re-supply station.
    print('Problem #4:\n{}'.format(probabilities(2, int(1e6))))