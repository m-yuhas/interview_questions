#!/usr/bin/env python


from itertools import combinations, combinations_with_replacement
from typing import List, Union


def six_digit_perfect_square() -> Union[int, None]:
    for i in range(300, 1000):
        j = i * i
        lsd = j % 1000
        msd = (j - lsd) // 1000
        if msd == lsd - 1:
            return j
        
def stamp_values(n: int, m: int, max_value: int) -> List[int]:
    for stamp_values in combinations([i for i in range(1, max_value + 1)], n):
        sums = [0] * max_value
        for i in range(m + 1):
            for c in combinations_with_replacement(stamp_values, i):
                if sum(c) < len(sums):
                    sums[sum(c)] += 1
        try:
            sums[1:].index(0)
        except ValueError as e:
            return stamp_values
    return False


def state_names() -> Union[str, None]:
    states = ['ALABAMA', 'ALASKA', 'ARIZONA', 'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']
    return_list = []
    for current_state in states:
        candidate = True
        for compare_state in states:
            shares_letter = False
            for letter in current_state.replace(' ', ''):
                if letter in compare_state.replace(' ', ''):
                    shares_letter = True
                    break
            if shares_letter == False:
                candidate = False
                break
        if candidate != False:
            return_list.append(current_state)
    smallest_name = return_list[0]
    for name in return_list:
        if len(name) < len(smallest_name):
            smallest_name = name
    return smallest_name

def probabilities(n: int, iterations: int) -> float:
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
    
    #print('Problem #2:\n{}'.format(stamp_values(7, 3, 71)))
    # IDEA: problem for permutation and combination
    # IDEA: problem for mean, media, mode, max/ min
    
    print('Problem #3:\n{}'.format(state_names()))
    
    print('Problem #4:\n{}'.format(probabilities(2, int(1e6))))