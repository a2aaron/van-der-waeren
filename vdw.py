#-*- coding: utf-8 -*-

import math
import random
# def is_VDW_string(string, colors, length):
#     for i in range(1, max_gap):
#         for j in range(0, len(string) - length):
            


# def max_gap(string_length, mono_length):
#     return math.floor(string_length / mono_length)

#


def is_simple_VDW(string):
    # Start must be 1 as we want to have a positive gap.
    upper_gap_bound = 1 + int(math.floor((len(string) - 1) / 2))
    for array in iter_simple_VDW(string):
        if all_same(array):
            return False
    return True

def iter_simple_VDW(string):
    # Start must be 1 as we want to have a positive gap.
    upper_gap_bound = 1 + int(math.floor((len(string) - 1) / 2))
    for gap in range(1, upper_gap_bound):
        for shift in range(0, len(string) - 2 * gap): 
            yield [string[shift], string[shift + gap], string[shift + 2*gap]]

def first_monochrome(string):
    upper_gap_bound = 1 + int(math.floor((len(string) - 1) / 2))
    for gap in range(1, upper_gap_bound):
        for shift in range(0, len(string) - 2 * gap): 
            if all_same([string[shift], string[shift + gap], string[shift + 2*gap]]):
                return [shift, shift + gap, shift + 2*gap]
    return None

def all_same(items):
    return all(x == items[0] for x in items)

def random_element(array):
    return random.choice(array)

def make_simple_VDW(string_len, colors):
    vdw_array = [random_element(colors)]*string_len
    while not is_simple_VDW(vdw_array):
        vdw_array[random_element(first_monochrome(vdw_array))] = random_element(colors)
        yield vdw_array


for i in range(1, 100000):
    for x in make_simple_VDW(i, ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]):
        if is_simple_VDW(x):
            print(str(i) + " | " + "".join(x))