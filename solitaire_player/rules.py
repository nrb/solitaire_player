from solitaire_player.deck import Card


def is_valid(current_card: Card, destination: Card) -> bool:
    """Checks two cards for a valid move

    A move is valid when:
        The color of the cards do not match
        The value of the current card is one less than the destination

    This function won't be used to determine if a move from the playing board
    to a suit pile is legal.
    """
    match = current_card.color == destination.color
    difference = destination.value - current_card.value
    if not match and difference == 1:
        return True
    else:
        return False
