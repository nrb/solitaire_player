"""
The board and associated structures that actually hold deck and piles
"""

import logging
from solitaire_player.deck import Deck


class Board:
    def __init__(self):
        self.deck = Deck()
        self.tableau = []
        for i in range(0, 7):
            self.tableau.append(Column())
        self.foundation = []
        for i in range(0, 4):
            self.foundation.append(FoundationPile())

    def deal(self) -> None:
        # TODO: Shuffle before dealing
        loop = 0
        # While the deck has > 28 cards, deal them to the columns
        while loop < 7:
            cards_placed = 0
            logging.debug("Starting loop #{}".format(loop))
            card = self.deck.draw()
            # Each pass should put the card in the first column face up
            self.tableau[loop].face_up.append(card)
            cards_placed += 1
            logging.debug("Placed card {} on column {}, face up".format(
                card, loop))

            # Remaining columns get their cards added face down
            remaining = self.tableau[loop + 1:]
            for index, column in enumerate(remaining):
                card = self.deck.draw()
                column.face_down.append(card)
                cards_placed += 1
                logging.debug("Placed card %s on column %s, face down",
                              card, (loop + 1 + index))
            logging.debug('%s cards placed this loop', cards_placed)
            loop += 1


class Column:
    def __init__(self):
        # Cards in the pile where faces are not visible to the player.
        self.face_down = []
        # Cards in the pile where faces are visible to the player.
        self.face_up = []

    def __len__(self) -> int:
        return len(self.face_down) + len(self.face_up)

    def __str__(self) -> str:
        out = []
        for card in self.face_up:
            out.append(str(card))
        out.insert(0, str(len(self.face_down)))
        return " ".join(out)


class TableauPile:
    pass


class FoundationPile:
    pass


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    board = Board()
    board.deal()
    for column in board.tableau:
        print(str(column))
