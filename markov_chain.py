__author__ = 'Nick Flanders'

import sys

# Generate a Markov Probability Chain for note relationships


# Data Definitions:
# An MTuple is a (Number, Number)

# Initiate dictionary
prob_dict = {}


def add_entry(line):
    """

    :rtype : Dictionary
    """
    pair_array = line.split(" ")
    key = pair_array[0]
    value = float(pair_array[1])
    key_array = key.strip("(").strip(")").split(",")
    prob_dict[(key_array[0], key_array[1])] = value


prob_file = open("markov_init.txt", 'r').read()
split_lines = prob_file.splitlines()
for line in split_lines:
    if line[0] != "#":
        add_entry(line)

print prob_dict

print prob_dict[('I','vii0')]


