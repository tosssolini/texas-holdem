class Player():
    def __init__(self, name, me):
        self.name = name
        self.chips = 3000
        self.me = me
        self.button = False
        self.big_blind = False
        self.small_blind = False
        self.bet = 0
        self.hand = []

    def set_button(self):
        self.button = True
    
    def set_big_blind(self):
        self.big_blind = True

    def set_small_blind(self):
        self.small_blind = True
    
    def add_bet(self, value):
        self.bet += value
        self.chips -= value

    def add_card(self, card):
        self.hand.append(card)

    def reset(self):
        self.hand = []
        self.bet = 0

    def add_chips(self, value):
        self.chips += value

