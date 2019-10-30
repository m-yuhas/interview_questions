#!/usr/bin/env python3

from random import randint
from numpy import mean, histogram
import matplotlib.pyplot as pp

hops_list = []
for i in range(0, 10000000):
    location = 10
    hops = 0
    while location != 0:
        location -= randint(1, location)
        hops += 1
    hops_list.append(hops)
print(mean(hops_list))
print(histogram(hops_list, bins=10, range=(0,10)))

#pp.yscale("log")
#pp.show()
