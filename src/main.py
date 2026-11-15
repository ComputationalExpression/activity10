"""Build a tune and print what the Tune class says about it.

CMPSC 100: Computational Expression, Activity 10

This file is provided. Run it with: uv run python src/main.py
"""

from tune import Tune


def main():
    """Add the notes of a short tune, then print its description, pitches and highest note."""
    tune = Tune("Hot Cross Buns")
    # Each pair is a note and how many beats it lasts
    song = [["E", 1], ["D", 1], ["C", 2], ["E", 1], ["D", 1], ["C", 2], ["X", 1]]
    for pair in song:
        if not tune.add(pair[0], pair[1]):
            print("Left out:", pair[0])
    print(tune.describe())
    print("Pitches:", tune.frequencies())
    print("Highest:", tune.highest())


main()
