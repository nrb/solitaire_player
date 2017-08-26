from typing import List, NamedTuple
import random

Card = NamedTuple('Card', [('suit', str),
                           ('face', str),
                           ('symbol', str),
                           ('value', int)
                           ])


class Deck():
    def __init__(self):
        self.suits = [('Hearts', '♥️'),
                      ('Diamonds', '♦️'),
                      ('Spades', '♠️'),
                      ('Clubs', '♣️')]

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
        for suit, symbol in self.suits:
            for face, val in card_values:
                card = Card(suit=suit, face=face, symbol=symbol, value=val)
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
