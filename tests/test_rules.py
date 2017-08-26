from solitaire_player.deck import Card
from solitaire_player import rules


def test_valid_move():
    dest_card = Card(suit='Heart', face='A', symbol='♥️',
                     color='red', value=13)
    curr_card = Card(suit='Spade', face='K', symbol='♠️',
                     color='black', value=12)
    assert rules.is_valid(curr_card, dest_card)


def test_invalid_move():
    curr_card = Card(suit='Heart', face='A', symbol='♥️',
                     color='red', value=13)
    dest_card = Card(suit='Spade', face='K', symbol='♠️',
                     color='black', value=12)
    assert not rules.is_valid(curr_card, dest_card)
