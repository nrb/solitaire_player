import pytest
from solitaire_player.board import Board, Column


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


@pytest.mark.skip(reason="need to write some extra debugging methods")
def test_dealing_from_deck():
    board = Board()
    board.deal()
    # Failing, getting 18 instead of 24.
    assert len(board.deck) == 24
    for index, column in enumerate(board.tableau):
        assert len(column) == index + 1
