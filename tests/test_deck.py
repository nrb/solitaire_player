from solitaire_player.deck import Deck


def test_creating_deck():
    deck = Deck()
    assert len(deck.cards) == 52


def test_finding_by_suit():
    deck = Deck()
    hearts = deck.cards_by_suit('Hearts')
    assert len(hearts) == 13
    assert all([c for c in hearts if c.suit == 'Hearts'])


def test_finding_by_face():
    deck = Deck()
    aces = deck.cards_by_face('A')
    assert len(aces) == 4
    assert all([c for c in aces if c.face == 'A'])


def test_shuffle():
    deck = Deck()
    first_five = deck.cards[:5]
    last_five = deck.cards[-5:]
    deck.shuffle()
    assert first_five != deck.cards[:5]
    assert last_five != deck.cards[-5:]
