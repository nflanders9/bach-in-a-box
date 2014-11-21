__author__ = 'Nick Flanders'
import chord_prog

# Correct any errors in the chord progression

def cad64_5_1(prog):
    """
    Return a chord progression with I chords following the V after a Cad64
    :param prog: [Listof [Listof Number]]
    :return: [Listof [Listof Number]]
    """
    for index in range(0, (len(prog)) - 1):
        if prog[index] == "CAD64" and len(prog) > 2 + index:
            prog = prog[:index + 2]
            new_chords = chord_prog.chord_prog(8 - len(prog))
            new_chords = cad64_5_1(new_chords)
            for chord in new_chords:
                prog.append(chord)
    return prog


for i in range(0, 10):
    chords = chord_prog.chord_prog(8)
    print chords
    print cad64_5_1(chords)
    print ""