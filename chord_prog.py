import markov_chain
from random import random, choice

__author__ = 'Nick Flanders'

# Generate a chord progression based on Markov probabilities

# Call on chord_prog(<number of chords>) to create a sequential chord progression list


def next_chord(last, dict):
    chord_list = ["I", "I6", "ii", "ii6", "iii", "IV", "V", "CAD64", "vi", "vii0", "vii06"]
    prob_list = []
    for chord in chord_list:
        prob_list.append(dict[(last, chord)])
    prob_list = make_cumulative(prob_list)
    rand_num = random()
    index = 0
    while True:
        if prob_list[index] >= rand_num:
            break
        index += 1
    return chord_list[index]


def make_cumulative(list, total = 0, index = 0):
    """
    Return a list of numbers that is cumulative from the left to right
    :param list: [Listof Number]
    :param total: Number (default is 0)
    :param index: Number (default is 0)
    :return: [Listof Number]
    """
    if len(list) == index:
        return list
    else:
        list[index] = list[index] + total
        new_total = list[index]
        index += 1
        return make_cumulative(list, new_total, index)


def chord_prog(num_chords):
    markov_dict = markov_chain.markov()
    chords = []
    last_chord = choice(["I", "I6", "ii", "ii6", "iii", "IV", "V", "CAD64", "vi", "vii0", "vii06"])
    while num_chords > 0:
        chord = next_chord(last_chord, markov_dict)
        chords.append(chord)
        last_chord = chord
        num_chords -= 1
    return chords



"""
Testing:

IV_tally = 0
ii6_tally = 0
for i in range(0, 1000):
    if next_chord("I6", markov_chain.markov()) == "IV":
        IV_tally += 1
    else:
        ii6_tally += 1
print "IV percentage:  " + str(IV_tally / 1000.0)
print "ii6 percentage:  " + str(ii6_tally / 1000.0)
"""
