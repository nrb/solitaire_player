from typing import List, NamedTuple

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

    def cards_by_suit(self, suit) -> List[Card]:
        return list(filter(lambda x: x.suit == suit, self.cards))

    def cards_by_face(self, face) -> List[Card]:
        return list(filter(lambda x: x.face == face, self.cards))
