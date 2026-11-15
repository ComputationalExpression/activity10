"""A tune for the buzzer: notes, how many beats each lasts, and their pitches.

CMPSC 100: Computational Expression, Activity 10

Author: TODO
"""

# Each note's pitch in hertz, the number a buzzer's freq() takes
NOTES = {"C": 262, "D": 294, "E": 330, "F": 349, "G": 392, "A": 440, "B": 494}


class Tune:
    """A titled tune: a list of notes and a list of how many beats each one lasts."""

    # TODO: Replace this line with # Copilot: accepted, # Copilot: edited or # Copilot: rejected
    def __init__(self, title):
        # TODO: Write a docstring: remember the title, and start with no notes and no beats
        # TODO: Assign title to self.title, and an empty list to self.notes and to self.beats
        pass

    # TODO: Replace this line with your Copilot decision
    def add(self, note, beats):
        # TODO: Write a docstring: add a note from NOTES with its beats and return True,
        # or return False for any other note
        # TODO: Use if and else. When note is a key of NOTES, append note to self.notes and
        # beats to self.beats, then return True. Otherwise, return False
        pass

    # TODO: Replace this line with your Copilot decision
    def length(self):
        # TODO: Write a docstring: return the total number of beats in the tune
        # TODO: Add up self.beats with a loop and return the total
        pass

    # TODO: Replace this line with your Copilot decision
    def frequencies(self):
        # TODO: Write a docstring: return a list of the pitch of each note, in order
        # TODO: Loop over self.notes, append each note's pitch from NOTES to a new list,
        # and return that list
        pass

    # TODO: Replace this line with your Copilot decision
    def highest(self):
        # TODO: Write a docstring: return the note with the highest pitch, or "none"
        # when the tune has no notes
        # TODO: Loop over self.notes and keep the best note so far and its pitch, as
        # most_common did in Activity 8. Start the best note at "none"
        pass

    # TODO: Replace this line with your Copilot decision
    def describe(self):
        # TODO: Write a docstring: return a line with the title, the number of notes,
        # and the number of beats
        # TODO: Return an f-string such as "Hot Cross Buns: 6 notes, 8 beats". Call
        # self.length() for the beats
        pass
