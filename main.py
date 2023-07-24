# Main
import random
import time

import player
import deck

def main():

    # Set up players
    players = []
    number_of_players = int(input("User input number of players (Max 5): "))
    my_name = input("Your name: ")
    players.append(player.Player(my_name, True))

    for i in range(number_of_players):
        if i != 0:
            name = input(f"Opponent {i} name: ")
            players.append(player.Player(name, False))
    
    # Create a deck
    my_deck = deck.Deck()

    # Set a table
    table = []

    # Set button:
    button = random.choice(range(number_of_players))
    big_blind = (button + 1) % (number_of_players)
    small_blind = (button + 2) % (number_of_players)
    blind = 10
    round_counter = 1

    # Game loop
    while True: 
        print(f"Round number {round_counter}")
        print(f"Big blind: {blind*2} ({players[big_blind].name})")
        print(f"Small blind: {blind} ({players[small_blind].name})")
   
        players[button].set_button == True
        players[big_blind].set_big_blind == True
        players[small_blind].set_small_blind == True

        for p in players:
            if p.big_blind == True:
                p.add_bet(2*blind)
            if p.small_blind == True:
                p.add_bet(blind)
            
        # Deal hands (random card select and update deck)
        print("Dealing cards")
        for i in range(2):
            for p in players:
                card = random.choice(my_deck.cards)
                p.add_card(card)
                my_deck.remove(card)
        
        # River
        for i in range(3):
            card = random.choice(my_deck.cards)
            table.append(card)
            my_deck.cards.remove(card)

        # Show river and user hand
        for p in players:
            print(f"Player {p.name}: {p.hand}")

        print(f"Table: {table}")         
        # User input call, raise, fold

        # Evaluate score (monte carlo?) 
        
        # Reset and prepare next round:
        for p in players:
            p.reset()
        table = []
        my_deck.reset()

        button = (button + 1) % (number_of_players)
        big_blind = (button + 1) % (number_of_players)
        small_blind = (button + 2) % (number_of_players)

        round_counter += 1
        if round_counter%5 == 0:
            blind*=2
        time.sleep(2)

if __name__ == "__main__":
    main()