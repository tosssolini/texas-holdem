class Deck():
    def __init__(self):
        self.cards = create_deck()

    def remove(self, card):
        self.cards.remove(card)

    def reset(self):
        self.cards = create_deck()

# Create deck
def create_deck():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suit = ["C", "D", "H", "S"]
    deck = []
    for s in suit:
        for v in values:
            deck.append(v+s)
    return deck