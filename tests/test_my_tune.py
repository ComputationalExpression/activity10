"""My tests for the Tune class.

Run them with: uv run pytest tests/test_my_tune.py
"""

from tune import Tune


def test_a_new_tune_has_no_notes():
    """A tune that was just made has its title, no notes, and no beats."""
    tune = Tune("Quiet")
    assert tune.title == "Quiet"
    assert tune.notes == []
    assert tune.length() == 0


# TODO: Replace this line with your Copilot decision
def test_add():
    # TODO: Write a docstring: what this test checks
    # TODO: Make a Tune, add a note from NOTES and one that is not, and assert what
    # add returns each time and what self.notes and self.beats hold afterward
    pass


# TODO: Replace this line with your Copilot decision
def test_length():
    # TODO: Write a docstring, then add two notes and assert the total of their beats
    pass


# TODO: Replace this line with your Copilot decision
def test_frequencies():
    # TODO: Write a docstring, then add two notes and assert the list of their pitches
    pass


# TODO: Replace this line with your Copilot decision
def test_highest():
    # TODO: Write a docstring, then assert the highest of three notes, with the highest
    # one in the middle, and what highest returns for a tune with no notes
    pass


# TODO: Replace this line with your Copilot decision
def test_describe():
    # TODO: Write a docstring, then add two notes and assert the line describe returns
    pass
