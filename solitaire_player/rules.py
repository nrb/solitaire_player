from solitaire_player.deck import Card


def is_valid(current_card: Card, destination: Card) -> bool:
    """Checks two cards for a valid move

    A move is valid when:
        The color of the cards do not match
        The value of the current card is one less than the destination

    This function won't be used to determine if a move from the playing board
    to a suit pile is legal.
    """
    # TODO: check for a card to a space is only Kings; maybe in the board?
    match = current_card.color == destination.color
    difference = destination.value - current_card.value
    if not match and difference == 1:
        return True
    else:
        return False


def is_valid_foundation(current_card: Card, destination: Card) -> bool:
    """Checks if a move from the tableau to the foundation is valid

    A move is valid when:
        The suit matches
        The value of the current card is one higher than the destination
    """
    # TODO: check for Ace to empty foundation slot; maybe in board?
    suit_match = current_card.suit == destination.suit
    difference = destination.value - current_card.value

    if suit_match and (difference == -1 or difference == 12):
        return True
    else:
        return False
