# A Solitaire Playing AI

The goal of this repo is to build up a solitaire game API, then model playing it with an AI.
It's currently incomplete, but the basic primitives such as cards, the deck, and the board/tableau are present.

Currently, there aren't plans for a GUI other than on the console, but that may come later.

The rules used will be from [Bicycle's description of the game](http://www.bicyclecards.com/how-to-play/solitaire/)

# Running the tests
You must have [tox](https://tox.readthedocs.io/en/latest/) installed, then simply run `tox` and the tests will run.

The current tests include flake8 syntax checking and linting, mypy type checking, and tests to ensure
that deck and board objects build correctly, as well as testing the current ruleset.
