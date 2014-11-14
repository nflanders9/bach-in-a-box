__author__ = 'Nick Flanders'

# Generate a Markov Probability Chain for note relationships


# Data Definitions:
# An MTuple is a (Number, Number)

import sys

def gen_markov(line):
    pair_array = line.split(" ")
    print pair_array

prob_file = open("markov_init.txt", 'r').read()
split_lines = prob_file.splitlines()
for line in split_lines:
    gen_markov(line)


