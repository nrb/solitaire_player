from solitaire_player.deck import Deck


def test_creating_deck():
    deck = Deck()
    assert len(deck.cards) == 52
