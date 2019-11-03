#!/usr/bin/env python


from random import randint
from sys import modules
from typing import List


try:
    from matplotlib import pyplot
except:
    pass



def simulate_river_crossing(n: int, iterations: int) -> float:
    """Simulate <iterations> number of river crossing with n lily pads.
    
    Arguments:
        n: int
            The number of lily pads in the river

        iterations: int
            The number of river crossings to simulate

    Returns:
        float: the mean of the number of hops of all simulated river crossings
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


def simulate_range_of_crossings(n_min: int,
                                n_max: int,
                                n_inc: int,
                                iterations: int) -> List[float]:
    """Simulate <iterations> number of river crossings from n_min lily pads to
    n_max lily pads.
    
    Arguments:
        n_min: int
            The lowest number of lily pads in the river
        n_max: int
            The highest number of lily pads in the river
        n_inc: int
            The resolution of the simulation
        iterations: int
            The number of river crossings to simulate for n

    Returns:
        List[float]: list of the mean number of hops for all n
    """
    means = []
    for i in range(n_min, n_max, n_inc):
        means.append(simulate_river_crossing(i, iterations))
    return means


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
    simulated_result = simulate_range_of_crossings(0, 100, 1, int(1e3))
    print('Problem #2:\n{}'.format(simulated_result))
    if 'matplotlib.pyplot' in modules:
        pyplot.plot(simulated_result)
        pyplot.xlabel('Number of lily pads in the river')
        pyplot.ylabel('Average number of hops to cross the river')
        pyplot.title('Simulated Results for the Frog Crossing the River')
        pyplot.show()
    
    # Problem 3:
    # Find a recurrence relation to find a the actual expected value of the
    # number of hops the frog will need to cross the river with n lily pads.
    
    # Problem 4:
    # Compare the error between the simulation and the recurrence relation for n
    # lily pads.  How many simulated river crossings are required to make the
    # error less than 1e-3?
