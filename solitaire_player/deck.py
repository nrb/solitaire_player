from typing import List, NamedTuple
import random

Card = NamedTuple('Card', [('suit', str),
                           ('face', str),
                           ('symbol', str),
                           ('color', str),
                           ('value', int)
                           ])


class Deck():
    def __init__(self):
        self.suits = [('Hearts', '♥️', 'red'),
                      ('Diamonds', '♦️', 'red'),
                      ('Spades', '♠️', 'black'),
                      ('Clubs', '♣️', 'black')]

        self.cards = self.build_deck()

    def build_deck(self) -> List[Card]:
        """Initialize the deck with a list of reified card objects"""
        card_faces = [
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'J',
            'Q',
            'K',
            'A',
        ]

        card_values = []

        for val, face in enumerate(card_faces, 1):
            card_values.append((face, val))

        cards = []
        for suit, symbol, color in self.suits:
            for face, val in card_values:
                card = Card(suit=suit, face=face, symbol=symbol, color=color,
                            value=val)
                cards.append(card)
        return cards

    def __contains__(self, card: Card) -> bool:
        return card in self.cards

    def cards_by_suit(self, suit: str) -> List[Card]:
        return list(filter(lambda x: x.suit == suit, self.cards))

    def cards_by_face(self, face: str) -> List[Card]:
        return list(filter(lambda x: x.face == face, self.cards))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> Card:
        """Draws the card at the top of the deck

        cards[51] is considered the top
        """
        return self.cards.pop()

    def draw_multiple(self, num: int) -> List[Card]:
        cards = self.cards[:num]
        self.cards = self.cards[num:]
        return cards

    def add(self, card: Card) -> None:
        """Places a card back on top of the deck"""
        self.cards.append(card)

    def __repr__(self) -> str:
        return str(self.cards)

    def __str__(self) -> str:
        """Print the current state of the deck w/o colors"""
        format_str = "{face}{symbol}"
        out = []
        for card in self.cards:
            out.append(format_str.format(face=card.face, symbol=card.symbol))
        return " ".join(out)

    def color_print(self) -> str:
        """Pretty-print the current state of the deck w/ terminal colors"""
        color_map = {'red': '\033[31m',
                     'black': '\033[30m'}
        end = '\033[0m'
        format_str = "{color}{face}{symbol}{end}"
        out = []
        for card in self.cards:
            out.append(format_str.format(face=card.face, symbol=card.symbol,
                                         color=color_map[card.color], end=end))
        return " ".join(out)


if __name__ == '__main__':
    # Some quick checks for visuals
    deck = Deck()
    print(str(deck))
    print(deck.color_print())
    deck.shuffle()
    print(str(deck))
    print(deck.color_print())
