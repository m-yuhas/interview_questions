#!/usr/bin/env python


from random import randint
from numpy import mean, histogram
import matplotlib.pyplot as pp


def simulate_river_crossing(n: int, iterations: int) -> float:
    """Simulate <iterations> number of river crossing with n lily pads.
    
    Arguments:
        n: int
            The number of lily pads in the river

        iterations: int
            The number of river crossings to simulate

    Returns:
        float: the mean of the number of hops of all simulated river crossings.
    """
    hops_list = []
    for i in range(iterations):
        location = n + 1
        hops = 0
        while location != 0:
            location -= randint(1, location)
            hops += 1
        hops_list.append(hops)
    return sum(hops_list) / len(hops_list)


if __name__ == '__main__':
    # Problem 1:
    # A frog is trying to cross a river.  There are nine lily pads forming a
    # path across the river.  It is equally likely that the frog will jump on
    # any of the lily pads including the opposing bank. Once the frog hops once,
    # it will continue moving forward, hopping on any of the remain lily pads or
    # the opposing bank with equal probability.  Create a simulation to find
    # the expected number of hops for the frog to cross the river.
    print('Problem #1:\n{}'.format(simulate_river_crossing(9, int(1e3))))

    # Problem 2:
    # Simulate the expected number of hops for the frog to cross the river with
    # n lily pads where n ranges from 0 to 100.
    
    # Problem 3:
    # Find a recurrence relation to find a the actual expected value of the
    # number of hops the frog will need to cross the river with n lily pads.
    
    # Problem 4:
    # Compare the error between the simulation and the recurrence relation for n
    # lily pads.  How many simulated river crossings are required to make the
    # error less than 1e-3?
