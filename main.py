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
    big_blind = (button - 1) % (number_of_players)
    small_blind = (button - 2) % (number_of_players)
    blind = 10
    round_counter = 1

    # Game loop
    while True: 
        print(f"Round number {round_counter}")
        print(f"Big blind: {blind*2} ({players[big_blind].name})")
        print(f"Small blind: {blind} ({players[small_blind].name})")
   
        players[button].set_button()
        players[big_blind].set_big_blind()
        players[small_blind].set_small_blind()

        for p in players:
            if p.big_blind:
                print("KUKKKE")
                p.add_bet(2*blind)
            if p.small_blind:
                p.add_bet(blind)
            
        # Deal hands (random card select and update deck) and flop
        print("Dealing cards")
        for i in range(2):
            for p in players:
                card = random.choice(my_deck.cards)
                p.add_card(card)
                my_deck.remove(card)
        
        for i in range(3):
            card = random.choice(my_deck.cards)
            table.append(card)
            my_deck.cards.remove(card)

        # Show hands and table
        show_table(players, table)

        # User input call, raise, fold

        for p in players:
            if p.is_me == True:
                choice = input("Do you want to call (c), raise (r) or fold (f)?: ")
                if choice == "r":
                    p.add_bet = input("How much do you want to raise?: ")
                elif choice == "f":
                    p.set_folded()
            else:
                choice = random.choice(["c", "r", "f"])
                if choice == "r":
                    p.add_bet = random.randrange(blind*2, blind*10, blind*2)
                elif choice == "f":
                    p.set_folded() 

        # Deal cards and river
        print("Dealing cards")
        for p in players:
            if not p.folded:
                card = random.choice(my_deck.cards)
                p.add_card(card)
                my_deck.remove(card)

        card = random.choice(my_deck.cards)
        table.append(card)
        my_deck.cards.remove(card)

        # Show hands and table
        show_table(players, table) 

        # User input call, raise, fold

        for p in players:
            if not p.folded:
                if p.is_me == True:
                    choice = input("Do you want to call (c), raise (r) or fold (f)?: ")
                    if choice == "r":
                        p.add_bet = input("How much do you want to raise?: ")
                    elif choice == "f":
                        p.set_folded()
                else:
                    choice = random.choice(["c", "r", "f"])
                    if choice == "r":
                        p.add_bet = random.randrange(blind*2, blind*10, blind*2)
                    elif choice == "f":
                        p.set_folded() 
        
        # Deal cards and turn
        print("Dealing cards")
        for p in players:
            if not p.folded:
                card = random.choice(my_deck.cards)
                p.add_card(card)
                my_deck.remove(card)

        card = random.choice(my_deck.cards)
        table.append(card)
        my_deck.cards.remove(card)

        # Show hands and table
        show_table(players, table)

        # User input call, raise, fold

        for p in players:
            if not p.folded:
                if p.is_me == True:
                    choice = input("Do you want to call (c), raise (r) or fold (f)?: ")
                    if choice == "r":
                        p.add_bet = input("How much do you want to raise?: ")
                    elif choice == "f":
                        p.set_folded()
                else:
                    choice = random.choice(["c", "r", "f"])
                    if choice == "r":
                        p.add_bet = random.randrange(blind*2, blind*10, blind*2)
                    elif choice == "f":
                        p.set_folded()

        # Evaluate score (monte carlo?) 
        
        # Reset and prepare next round:
        for p in players:
            p.reset()
        active_players = players
        table = []
        my_deck.reset()

        button = (button + 1) % (number_of_players)
        big_blind = (button - 1) % (number_of_players)
        small_blind = (button - 2) % (number_of_players)

        round_counter += 1
        if round_counter%5 == 0:
            blind*=2
        time.sleep(2)


def show_table(players, table):
    for p in players:
        print(f"Player {p.name}: {p.hand}, Bet: {p.bet}, Chips: {p.chips}")
    print(f"Table: {table}")    


if __name__ == "__main__":
    main()