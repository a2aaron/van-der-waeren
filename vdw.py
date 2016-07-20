#-*- coding: utf-8 -*-

import math
import random

'''
A simple VDW string is a string that contains no instance
of three of the same characters equally spaced apart. 
For example, "rrbrbr" NOT a VDW string because you can find
three "r"s that are equally spaced apart.
'''
def is_simple_VDW(string):
    if not string:
        return False
    # Start must be 1 as we want to have a positive gap.
    upper_gap_bound = 1 + int(math.floor((len(string) - 1) / 2))
    for array in iter_simple_VDW(string):
        if all_same(array):
            return False
    return True

'''
Iterates through a potential simple VDW string. It returns
an array of three characters equally spaced apart. It eventually
iterates through all possibilities.
'''
def iter_simple_VDW(string):
    # Start must be 1 as we want to have a positive gap.
    upper_gap_bound = 1 + int(math.floor((len(string) - 1) / 2))
    for gap in range(1, upper_gap_bound):
        for shift in range(0, len(string) - 2 * gap): 
            yield [string[shift], string[shift + gap], string[shift + 2*gap]]


'''
Return the first instance of a monochrome string in a possible VDW string.
For example, "rrbrbr" will return [1, 2, 3]
'''
def first_monochrome(string):
    upper_gap_bound = 1 + int(math.floor((len(string) - 1) / 2))
    for gap in range(1, upper_gap_bound):
        for shift in range(0, len(string) - 2 * gap): 
            if all_same([string[shift], string[shift + gap], string[shift + 2*gap]]):
                return [shift, shift + gap, shift + 2*gap]
    return None


'''Returns true if all the elements are the same value (likely casts)'''
def all_same(items):
    return all(x == items[0] for x in items)

def random_element(array):
    return random.choice(array)


'''Return a valid VDW string given the required
string length and number of colors'''
def make_simple_VDW(string_len, colors):
    # Make a random array start
    vdw_array = [random_element(colors)]*string_len
    while not is_simple_VDW(vdw_array):
        # If the string isn't VDW, take the first possible monochrome instance
        # and change a random triple to a random color.
        vdw_array[random_element(first_monochrome(vdw_array))] = random_element(colors)
    return "".join(vdw_array)