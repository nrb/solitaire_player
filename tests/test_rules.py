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


def test_invalid_foundation_move():
    dest_card = Card(suit='Spade', face='K', symbol='♠️',
                     color='black', value=12)
    curr_card = Card(suit='Spade', face='Q', symbol='♠️',
                     color='black', value=11)
    assert not rules.is_valid_foundation(curr_card, dest_card)


def test_valid_foundation_move():
    curr_card = Card(suit='Spade', face='K', symbol='♠️',
                     color='black', value=12)
    dest_card = Card(suit='Spade', face='Q', symbol='♠️',
                     color='black', value=11)
    assert rules.is_valid_foundation(curr_card, dest_card)


def test_two_to_ace_move():
    curr_card = Card(suit='Spade', face='2', symbol='♠️',
                     color='black', value=1)
    dest_card = Card(suit='Spade', face='A', symbol='♠️',
                     color='black', value=13)
    assert rules.is_valid_foundation(curr_card, dest_card)


def test_two_to_king_move():
    curr_card = Card(suit='Spade', face='2', symbol='♠️',
                     color='black', value=1)
    dest_card = Card(suit='Spade', face='K', symbol='♠️',
                     color='black', value=12)
    assert not rules.is_valid_foundation(curr_card, dest_card)
