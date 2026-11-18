# Activity 10: Tab to Accept

|Item |       |
|:----|:------|
|Released |Wednesday, November 18, in class |
|Due |Monday, November 23, 9:00am |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

In this activity you write a `Tune` class with GitHub Copilot's code completion turned on, and
then write tests that check it. Copilot suggests code in gray as you type, and you decide what
to keep. A tune is a list of notes and how many beats each one lasts, and each note has a pitch
in hertz, the number a buzzer plays. If a step confuses you, please ask about it while you are
still in the room.

## Course learning outcomes

This activity addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

**CLO 4.** Evaluate the practical and ethical implications of writing computer code and discuss the
contexts, perceived effects, and impacts exerted on and by computer code as a cultural force or
artifact.

Specifically, by the end of this activity you should be able to:

* accept a code suggestion with `Tab`, and edit or reject it
* write a test with `assert` and run it with `pytest`
* explain why a test needs to fail when the code it checks is wrong

## Turn on code completion

This repository turns on Copilot's code completion and leaves Copilot Chat's agent off. First open the
Extensions view, search for `Copilot`, and install **GitHub Copilot Chat** if it is not installed yet. It
includes code completion. To sign in, click the Copilot icon in the bar along the bottom of VS Code and sign in with your GitHub
account. If you do not see the icon, click the gear icon at the bottom left of VS Code, choose **Settings**, search for `Disable AI Features`, and
uncheck it.

|What you want |Mac |Windows |
|:-------------|:---|:-------|
|Accept a suggestion |`Tab` |`Tab` |
|Reject a suggestion |`Esc`, or keep typing |`Esc`, or keep typing |
|Extra: accept the next word |`Cmd` + `Right Arrow` |`Ctrl` + `Right Arrow` |
|Extra: see a different suggestion |`Option` + `]` |`Alt` + `]` |

Keyboard shortcuts can differ from one machine to another. Rely on `Tab` and `Esc`; the extras
may not work on every computer.

## The rules

1. Read a suggestion before you press `Tab`. When Copilot suggests several lines at once, press
   `Esc` and keep typing, so each suggestion is short enough to check.
2. Keep only what you can explain. If a suggestion uses something we have not covered, such as
   `sum`, `max` or `sorted`, reject it and write the loop yourself.
3. Record your decision by replacing the `TODO` line above each `def` with one of these:
   * `# Copilot: accepted` when you kept the suggestions as they were
   * `# Copilot: edited` when you kept some and changed or wrote the rest
   * `# Copilot: rejected` when you wrote the method yourself

## Part 1: The Tune class

Open `src/tune.py`. `NOTES` maps each note to its pitch, and the `Tune` class has six methods for
you to write. For each one, write the docstring first, since Copilot reads it to decide what to
suggest, and then the body. The examples are also where the expected values for your tests in
Part 2 come from:

|Method |What it does |Example |
|:------|:------------|:-------|
|`__init__(title)` |Remembers the title, and starts `self.notes` and `self.beats` as empty lists |`Tune("Lullaby")` has title `"Lullaby"`, notes `[]` and beats `[]` |
|`add(note, beats)` |Appends a note from `NOTES` and its beats and returns `True`, or returns `False` for any other note |`add("F", 2)` returns `True`, and then notes is `["F"]` and beats is `[2]`; `add("H", 1)` returns `False` |
|`length()` |Returns the total number of beats |After `add("D", 2)` and `add("A", 1)`, returns `3` |
|`frequencies()` |Returns a list of the pitch of each note, in order |After `add("G", 1)` and `add("E", 2)`, returns `[392, 330]` |
|`highest()` |Returns the note with the highest pitch, or `"none"` when there are no notes |With notes D, A and C, returns `"A"`; with no notes, returns `"none"` |
|`describe()` |Returns a line such as `Hot Cross Buns: 6 notes, 8 beats` |For `Tune("Waltz")` after `add("F", 2)` and `add("C", 3)`, returns `"Waltz: 2 notes, 5 beats"` |

`src/main.py` is provided. Run it to see your class at work:

```text
$ uv run python src/main.py
Left out: X
Hot Cross Buns: 6 notes, 8 beats
Pitches: [330, 294, 262, 330, 294, 262]
Highest: E
```

## Part 2: Your tests

Open `tests/test_my_tune.py`. The first test is written for you as an example. Write the other
five, one for each method, with the same rules for Copilot. Run your tests with:

```text
uv run pytest tests/test_my_tune.py
```

A test is useful when it fails on wrong code. To check yours, five of the checks break one
method of your `Tune` on purpose, so that it skips its work and returns `None`, and then run
your tests again. Each of those checks passes when at least one of your tests fails.

## Evaluation

In-class activities are graded on completion and contribute to the **In-Class Activities**
category on the syllabus (10 points, averaged across the semester). This activity is worth one
activity grade. What is graded is your attempt, and a value that comes out wrong still counts toward it.

|Level |What it looks like |
|:-----|:------------------|
|**Complete** |At least half of the activity is done |
|**Partial** |Less than half is done, but something beyond the starter was committed |
|**Incomplete** |The starter was not changed |

Run the automated checks yourself, as many times as you like, from the top folder of this
repository:

```text
uv run gatorgrade --config gatorgrade.yml
```

Each check's description says what to look at when it fails. Under a failed check, gatorgrade
also prints a `uv run pytest ...` command, and when you run it, the last lines say what was
expected and what came back.

> [!NOTE]
> Automated results are preliminary. Your instructor sets the final grade.

## Submitting

Commit and push often. The last version pushed before the deadline is the one that gets
graded.

**In the terminal:**

```text
git add src/tune.py tests/test_my_tune.py
git commit -m "Write the Tune class and its tests"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it, which is `git add`
2. Type a message in the box at the top, then click the checkmark, which is `git commit`
3. Click **Sync Changes** (or the up arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are there.

If you need more time, apply a late token with [this form](https://forms.gle/3nGbpaNrG96DpLLdA).
