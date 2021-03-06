from solitaire_player.deck import Card, Deck


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


def test_drawing_card():
    deck = Deck()
    top = deck.cards[-1]
    card = deck.draw()
    assert card not in deck.cards
    assert card is top


def test_drawing_multiple_cards():
    deck = Deck()
    top_five = deck.cards[:5]
    cards = deck.draw_multiple(5)
    assert top_five == cards
    assert len(deck.cards) == 47


def test_adding_card():
    deck = Deck()
    card = deck.cards.pop()
    deck.add(card)
    assert card in deck.cards


def test_contains():
    deck = Deck()
    card = deck.cards[0]
    assert card in deck


def test_contains_fails():
    deck = Deck()
    # Even if there is a card with the same values, it's not the same object
    card = Card(suit='Heart', face='A', symbol='♥️', color='red', value=13)
    assert card not in deck


def test_deck_len():
    assert len(Deck()) == 52


def test_card_stringing():
    card = Card(suit='Heart', face='A', symbol='♥️', color='red', value=13)
    result = str(card)
    assert result == 'A♥️'


def test_card_color_print():
    card = Card(suit='Heart', face='A', symbol='♥️', color='red', value=13)
    result = card.color_print()
    assert result == '\033[31mA♥️\033[0m'


def test_deck_stringing():
    deck = Deck()
    result = str(deck)
    assert result.startswith('2♥️')
    assert result.endswith('A♣️')


def test_deck_color_printing():
    deck = Deck()
    result = deck.color_print()
    assert result.startswith('\033[31m2♥️\033[0m ')
    assert result.endswith('\033[30mA♣️\033[0m')
