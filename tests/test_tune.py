"""Checks for Activity 10: the Tune class in src/tune.py.

These are the instructor's tests. Your own tests go in tests/test_my_tune.py.
"""

from tune import NOTES, Tune


def build(title, pairs):
    """Return a Tune with each [note, beats] pair added to it."""
    tune = Tune(title)
    for pair in pairs:
        tune.add(pair[0], pair[1])
    return tune


def test_add_and_length():
    assert NOTES["A"] == 440 and len(NOTES) == 7, "please keep NOTES as it is in the starter"
    tune = Tune("Check")
    assert tune.title == "Check", "Tune('Check').title should be 'Check'"
    assert tune.notes == [] and tune.beats == [], "a new Tune should start with self.notes = [] and self.beats = []"
    assert tune.length() == 0, "a new Tune's length() should be 0"
    assert tune.add("G", 2) is True, "add('G', 2) should return True, since G is a key of NOTES"
    assert tune.add("H", 1) is False, "add('H', 1) should return False, since H is not a key of NOTES"
    assert tune.add("E", 3) is True, "add('E', 3) should return True"
    assert tune.notes == ["G", "E"], f"after adding G, H and E, self.notes should be ['G', 'E'], not {tune.notes}"
    assert tune.beats == [2, 3], f"after adding G for 2 and E for 3, self.beats should be [2, 3], not {tune.beats}"
    assert tune.length() == 5, f"with beats [2, 3], length() should be 5, not {tune.length()}"


def test_frequencies():
    tune = build("Pitches", [["A", 1], ["C", 2], ["A", 1]])
    found = tune.frequencies()
    assert found == [440, 262, 440], f"for notes A, C, A, frequencies() should be [440, 262, 440], not {found}"
    assert Tune("Empty").frequencies() == [], "a tune with no notes should give frequencies() == []"


def test_highest():
    for pairs, expected in [
        ([["C", 1], ["B", 1], ["E", 1]], "B"),
        ([["A", 1], ["D", 1]], "A"),
        ([["F", 1], ["G", 1]], "G"),
    ]:
        names = [pair[0] for pair in pairs]
        found = build("High", pairs).highest()
        assert found == expected, f"for notes {names}, highest() should be '{expected}', not {found!r}"
    found = Tune("Empty").highest()
    assert found == "none", f"a tune with no notes should give highest() == 'none', not {found!r}"


def test_describe():
    found = build("Short", [["D", 2], ["E", 1]]).describe()
    assert isinstance(found, str), "describe() should return a string, not print one"
    lowered = found.lower()
    assert "short" in lowered, f"describe() should include the title, Short; it returned {found!r}"
    assert "2 notes" in lowered, f"describe() should include '2 notes' for two notes; it returned {found!r}"
    assert "3 beats" in lowered, f"describe() should include '3 beats' for 2 + 1 beats; it returned {found!r}"
