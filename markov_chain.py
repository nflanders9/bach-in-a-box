import math
import sys

__author__ = 'Nick Flanders'

# Generate a Markov Probability Chain for note relationships


def add_entry(line):
    """
    Parse the string containing the dictionary data and add the value to the dictionary
    :param line: String
    :rtype : Dictionary
    """
    pair_array = line.split(" ")
    key = pair_array[0]
    value = float(pair_array[1])
    key_array = key.strip("(").strip(")").split(",")
    prob_dict[(key_array[0], key_array[1])] = value



def valid_input(list_of_lines):
    """
    Determine if the Markov chain data is valid
    :rtype : Boolean
    :param list_of_lines:
    """
    valid = True
    list_of_probs = []
    for line in list_of_lines:
        if line[0] == "@":
            if math.fabs(sum(list_of_probs) - 1.0) > .001:
                valid = False
                break
            else:
                list_of_probs = []
        if line[0] == "(":
            prob = float(line.split(" ")[1])
            list_of_probs.append(prob)
    return valid





def markov():
    """
    Return a dictionary with the probability data in markov_init.txt
    :rtype: Dictionary
    """
    # Initiate dictionary
    global prob_dict
    prob_dict = {}
    prob_file = open("markov_init.txt", 'r').read()
    split_lines = prob_file.splitlines()
    if valid_input(split_lines):
        for line in split_lines:
            if line[0] != "#" and line[0] != "@":
                add_entry(line)
        return prob_dict
    else:
        return 'Error: Invalid probability values in Markov Chain data file.'
