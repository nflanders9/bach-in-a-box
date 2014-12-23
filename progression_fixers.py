__author__ = 'Nick Flanders'
import markov_chain, chord_prog
# Correct any errors in the chord progression

def cad64_5_1(prog):
    """
    Return a chord progression with I chords following the V after a Cad64
    :param prog: [Listof [Listof Number]]
    :return: [Listof [Listof Number]]
    """
    for index in range(0, len(prog)):
        if prog[index] == "CAD64" and len(prog) > 2 + index:
            prog = prog[:index + 2]
            new_chords = chord_prog.chord_prog(8 - len(prog))
            new_chords = cad64_5_1(new_chords)
            for chord in new_chords:
                prog.append(chord)
        elif prog[index] == "CAD64" and len(prog) <= (2 + index):
            prog = prog[:index + 1]
            prog.append("V")
            prog.append("I")
    return prog


def end_on_I(prog, dict):
    while prog[len(prog) - 1] != "I":
        last_chord = prog[len(prog) - 1]
        if dict[(last_chord, "I")] != 0:
            prog.append("I")
            break
        else:
            prog.append(chord_prog.next_chord(last_chord, dict))
    return prog

def get_notes():
    dictionary = markov_chain.markov()
    return chord_prog.note_prog(end_on_I(cad64_5_1(chord_prog.chord_prog(8)), dictionary))

# Testing:
dictionary = markov_chain.markov()
chords = end_on_I(cad64_5_1(chord_prog.chord_prog(8)), dictionary)
print "Chord representation:"
print chords
notes = chord_prog.note_prog(chords)
print "Note progression:"
print notes
print get_notes()
