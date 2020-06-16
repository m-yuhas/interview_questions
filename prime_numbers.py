#/usr/bin/env python


from math import log2
from typing import List
from random import uniform
from statistics import mean


def get_primes(n: int) -> List[int]:
    """Return a list of all prime numbers less than n.
    
    This function determines if each integer is prime with efficiency
    O(sqrt(n)).  Memory consumption for each prime is O(1).
    
    Arguments:
        n: int
            Maximum number for the prime search

    Returns:
        List[int]: list of prime numbers
    """
    prime_list = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, round(i ** (1 / 2)) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            prime_list.append(i)
    return prime_list


def get_sequential_primes(addends: List[int], n: int ) -> List[int]:
    """Return a list of all prime numbers less than n for which the sum of the
    prime and any number in addends is also prime.
    
    Arguments:
        subsequent_primes: List[int]
            List of integers that when added to a prime number must yield a sum
            which is also prime
        n: int
            Maximum number for the prime search

    Returns:
        List[int]: list of prime numbers that when added to each integer in
            subsequent_primes yields a prime number
    """
    initial_primes = get_primes(n + max(addends))
    final_primes = []
    for i in initial_primes:
        match = True
        for j in addends:
            if i + j not in initial_primes:
                match = False
        if match:
            final_primes.append(i)
    return final_primes


def get_mersenne_primes(n: int) -> List[int]:
    """Return a list of all Mersenne primes less than n.  This function uses the
    Lucas-Lehmer primality test to determine if a number is prime.  Because the
    Lucas-Lehmer test only works for Mersenne numbers with odd primes, the value
    3 is hardcoded

    Arguments:
        n: int
            Maximum number for the Mercen prime search

    Returns:
        List[int]: list of Mercen primes less than n
    """
    primes = [3] if n > 3 else []
    m = 1
    last_s = 4
    max_m = log2(n - 1)
    while m < max_m:
        m += 1
        candidate = (2 ** m) - 1
        if last_s % candidate == 0:
            primes.append(candidate)
        last_s = (last_s ** 2) - 2
    return primes


def penguin_order(n: int) -> List[int]:
    """Get the order of penguins in the queue when each gets in line at the
    greatest m < n that divides n where n is an individual penguin's ticket
    number.
    
    Argument:
        n: int
            Number of penguins lining up in the queue

    Returns:
        List[int]: list of integers representing the order of penguins in the
            queue, where each integer corresponds to that penguins ticket number
    """
    queue = []
    for i in range(1, n + 1):
        if len(queue) == 0:
            queue.append(i)
            continue
        temp_queue = queue.copy()
        while len(temp_queue) > 0:
            if i % max(temp_queue) == 0:
                queue.insert(queue.index(max(temp_queue)) + 1, i)
                break
            else:
                temp_queue.pop(temp_queue.index(max(temp_queue)))
    return queue


if __name__ == '__main__':
    # Problem 1:
    # List all prime numbers less than 1000.
    print('Problem #1:\n{}'.format(get_primes(1000)))
    
    # Problem 2:
    # List all prime numbers less than 1000 for which p + 2, p + 6, p + 8 and
    # p + 12 are also prime
    print('Problem #2:\n{}'.format(get_sequential_primes([2, 6, 8, 12], 1000)))

    # Problem 3:
    # List all Mersenne primes less than 1000.
    print('Problem #3:\n{}'.format(get_mersenne_primes(1000)))

    # Problem 4:
    # There are 2019 penguins waddling toward their favorite restaurant.  As the
    # penguins arrive, they are handed tickets numbered in ascending order from
    # 1 to 2019, and told to join the queue.  The first penguin starts the
    # queue. For each n > 1, the penguin holding ticket number n finds the
    # greatest m < n which divides n and enters the queue directly behind the
    # penguin holding ticket number m.  This continues until all the penguins
    # are in the queue.  What is the order of penguins in the queue?
    print('Problem #3:\n{}'.format(penguin_order(2019)))