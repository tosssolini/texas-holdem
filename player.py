class Player():
    def __init__(self, name, me):
        self.name = name
        self.chips = 3000
        self.me = me
        self.button = False
        self.big_blind = False
        self.small_blind = False

    def set_button(self):
        self.button = True
    
    def set_big_blind(self):
        self.big_blind = True

    def set_small_blind(self):
        self.small_blind = True

    def set_me(self):
        self.me = True