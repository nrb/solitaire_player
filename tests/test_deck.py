from solitaire_player.deck import Deck


def test_creating_deck():
    deck = Deck()
    assert len(deck.cards) == 52


def test_finding_by_suit():
    deck = Deck()
    hearts = deck.cards_by_suit('Hearts')
    assert len(hearts) == 13
    assert all([c for c in hearts if c.suit == 'Hearts'])
