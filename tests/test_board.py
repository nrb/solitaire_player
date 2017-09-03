from solitaire_player.board import Board, Column
from solitaire_player.deck import Card


def test_board_has_all_pile_types():
    board = Board()
    assert hasattr(board, 'deck')
    assert hasattr(board, 'tableau')
    assert hasattr(board, 'foundation')


def test_board_has_correct_number_of_piles():
    board = Board()
    assert len(board.tableau) == 7
    assert len(board.foundation) == 4


def test_column_has_faceup_and_facedown():
    c = Column()
    assert hasattr(c, 'face_up')
    assert hasattr(c, 'face_down')


def test_column_has_len():
    c = Column()
    assert len(c) == 0


def test_column_string_no_face_up():
    c = Column()
    assert str(c) == '0'


def test_column_string_one_face_up():
    c = Column()
    card = Card(suit='Heart', face='A', symbol='♥️', color='red', value=13)
    c.face_up.append(card)
    assert str(c) == '0 A♥️'


def test_column_string_two_face_up():
    c = Column()
    card = Card(suit='Heart', face='A', symbol='♥️', color='red', value=13)
    c.face_up.append(card)
    card = Card(suit='Heart', face='K', symbol='♥️', color='red', value=12)
    c.face_up.append(card)
    assert str(c) == '0 A♥️ K♥️'


def test_dealing_from_deck():
    board = Board()
    board.deal()
    # Failing, getting 18 instead of 24.
    assert len(board.deck) == 24
    for index, column in enumerate(board.tableau):
        assert len(column) == index + 1
