__author__ = 'Nick Flanders'
import progression_fixers
import midi
import midi_dicts

frequencies = midi_dicts.frequencies

def give_key(prog, key):
    lookup = ["A", "B", "C", "D", "E", "F", "G"]
    key = key.upper()
    shift = ord(key) - 65
    new_prog = []
    for chord in prog:
        new_chord = []
        for note in chord:
            new_note = lookup[(note - 1 + shift) % 7]
            new_chord.append(new_note)
        new_prog.append(new_chord)
    return new_prog


# NOTE:
#     This is an incomplete implementation that does not take into account
#     the rhythm or th correct octave to play each note in
def to_midi(notes):
    # Instantiate a MIDI Pattern (contains a list of tracks)
    pattern = midi.Pattern()
    for i in range(0, 4):
        # Instantiate a MIDI Track (contains a list of MIDI events)
        track = midi.Track()
        # Append the track to the pattern
        pattern.append(track)
        for chord in notes:
            keyword = chord[i] + "_" + str(int(3 + i/2))
            # Instantiate a MIDI note on event, append it to the track
            on = midi.NoteOnEvent(tick=0, velocity=50, pitch=frequencies[keyword])
            track.append(on)
            # Instantiate a MIDI note off event, append it to the track
            off = midi.NoteOffEvent(tick=600, pitch=frequencies[keyword])
            track.append(off)
        # Add the end of track event, append it to the track
        eot = midi.EndOfTrackEvent(tick=1)
        track.append(eot)
    # Print out the pattern
    print pattern
    # Save the pattern to disk
    midi.write_midifile("output.mid", pattern)


notes = progression_fixers.get_notes()
to_midi(give_key(notes, "A"))