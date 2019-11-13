#!/usr/bin/env python


from random import randint
from sys import modules
from typing import List


try:
    from matplotlib import pyplot
except:
    pass


def simulate_average_hops(n_lily_pads: List[int],
                          iterations: int) -> List[float]:
    """Simulate <iterations> number of river crossing for each n lily pads in
    <n_lily_pads> and return a list of the average number of hops for each n.
    
    Arguments:
        n_lily_pads: List[int]
            A list of all numbers of lily pads in the river for which the
            average number of hops should be simulated

        iterations: int
            The number of river crossings to simulate

    Returns:
        List[float]: the average number of hops to cross the river for each
            number of lily pads provided in n_lily_pads
    """
    means = []
    for n in n_lily_pads:
        hops_list = []
        for i in range(iterations):
            location = n + 1
            hops = 0
            while location != 0:
                location -= randint(1, location)
                hops += 1
            hops_list.append(hops)
        means.append(sum(hops_list) / len(hops_list))
    return means


def actual_expected_hops(n_lily_pads: List[int]) -> List[float]:
    """Return the actual expected value of the number of hops the frog will need
    to cross the river for each n lily pads in <n_lily_pads>.
    
    Here it is fairly straightforward to derive the recurrence relation:
    
    E(n) = 1 + (1/(n+1))*sum(E(m)) where E(m) is summed from m = 0 to n - 1.
    
    However, this means that to calculate the expected value for any given n, we
    would have to sum all the previous expected values.  This could be
    accomplished by dynamic programming and keeping a running sum of the
    expected values as the results list is generated.  The other option is to
    use algebra and pull E(n-1) out from summation.  After this step we multiply
    both sides by (n + 1)/n and then subtract 1/n to transform the summation
    into another E(n-1) term.  Simplifying this equation yields the recurrence
    relation:
    
    E(n) = 1/(n+1) + E(n-1),
    
    which is calculated in this function for all provided n.
    
    Arguments:
        n_lily_pads: List[int]
            A list of all numbers of lily pads in the river for which the
            average number of hops should be simulated

    Returns:
        List[float]: the expected number of hops to cross the river for each
            number of lily pads provided in n_lily_pads
    """
    expected = [1]
    for n in range(1, max(n_lily_pads) + 1):
        expected.append((1/(n + 1)) + expected[-1])
    final = []
    for n in n_lily_pads:
        final.append(expected[n])
    return final


def simulate_pmf(n: int, iterations: int) -> List[float]:
    """Simulate the frog crossing a river with n lily pads <iterations> times
    and return the pmf for the probability of number of hops to cross the river.
    
    Arguments:
        n: int
            The number of lily pads to use in this simulation
        iterations: int
            The number of iterations to use for this simulation

    Returns:
        List[float]: list of floats representing the probability that the frog
            takes <index> hops to cross the river.
    """
    raw_counts = [0 for i in range(n + 2)]
    for i in range(iterations):
        location = n + 1
        hops = 0
        while location != 0:
            location -= randint(1, location)
            hops += 1
        raw_counts[hops] += 1
    return [raw_counts[i] / sum(raw_counts) for i in range(n + 2)]


def get_pmf(n: int) -> List[float]:
    """Return the pmf for the number of hops it takes the frog to cross a river
    with n lily pads.
    
    For n lily pads this can be expressed as the product of n sums.  This method
    uses recursion to calculate this value.

    Arguments:
        n: int
            The number of lily pads in the river

    Returns:
        List[float]: list of floats representing the probability that the frog
            takes <index> hops to cross the river.
    """

    def inner_sum(min: int, max: int) -> float:
        """Calculate the inner sum recursively.
        
        Arguments:
            min: int
                lower limit of the first sum
            max: int
                upper limit of the first sum

        Returns:
            float: the inner sum needed to calculate pmf(i)
        """
        if min == 0:
            return 1.0
        total = 0
        for i in range(min, max + 1):
            total += (1 / i) * inner_sum(min - 1, i - 1)
        return total

    pmf = [0.0]
    for i in range(1, n + 2):
        pmf.append((1 / (n + 1)) * inner_sum(i - 1, n))
    return pmf


if __name__ == '__main__':
    n_range = range(0, 100)
    
    # Problem 1:
    # A frog is trying to cross a river.  There are n lily pads forming a
    # path across the river.  It is equally likely that the frog will jump on
    # any of the lily pads including the opposing bank. Once the frog hops once,
    # it will continue moving forward, hopping on any of the remain lily pads or
    # the opposing bank with equal probability.  Create a simulation to find
    # the expected number of hops for the frog to cross the river for 0 to 99
    # lily pads.
    simulated_average = simulate_average_hops(n_range, int(1e3))
    print('Problem #1:\n{}'.format(simulated_average))
    if 'matplotlib.pyplot' in modules:
        pyplot.plot(simulated_average)
        pyplot.xlabel('Number of lily pads in the river')
        pyplot.ylabel('Average number of hops to cross the river')
        pyplot.title('Simulated Results for the Frog Crossing the River')
        pyplot.show()

    # Problem 2:
    # Find a recurrence relation to find the actual expected value of the number
    # of hops the frog will need to cross the river with n lily pads.
    actual_expected = actual_expected_hops(n_range)
    print('Problem #2:\n{}'.format(actual_expected))
    if 'matplotlib.pyplot' in modules:
        pyplot.plot(n_range, simulated_average, 'b', label='Simulated Average')
        pyplot.plot(n_range, actual_expected, 'r', label='Expected Value')
        pyplot.xlabel('Number of lily pads in the river')
        pyplot.ylabel('Number of hops to cross the river')
        pyplot.title('Simulated Results vs. Recurrence Relation')
        pyplot.legend()
        pyplot.show()
    
    # Problem 3:
    # Simulate the probability of the frog taking m hops to cross a river with 9
    # lily pads.  In other words, simulate probability mass function for number
    # of hops to cross the river.
    simulated_pmf = simulate_pmf(9, int(1e3))
    print('Problem #3:\n{}'.format(simulated_pmf))
    if 'matplotlib.pyplot' in modules:
        pyplot.plot(range(11), simulated_pmf, 'bo')
        pyplot.xlabel('Number of hops to cross the river')
        pyplot.ylabel('Probability')
        pyplot.title('Simulated PMF for the Number of Hops to Cross the River')
        pyplot.show()
    
    # Problem 4:
    # Find a recurrence relation that provides the exact probability mass
    # function for the number of hops it takes to cross the river.
    actual_pmf = get_pmf(9)
    print('Problem #4:\n{}'.format(actual_pmf))
    if 'matplotlib.pyplot' in modules:
        pyplot.plot(range(11), simulated_pmf, 'bo', label='Simulated PMF')
        pyplot.plot(range(11), actual_pmf, 'ro', label='Actual PMF')
        pyplot.xlabel('Number of hops to cross the river')
        pyplot.ylabel('Probability')
        pyplot.title('Simulated PMF vs. Actual PMF')
        pyplot.show()