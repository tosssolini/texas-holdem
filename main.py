# Main

import player

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
    

    # Create deck

    # Game loop:

    # Deal hands (random card select and update deck)

    # User input call, raise, fold

    # Evaluate score (monte carlo?) 

if __name__ == "__main__":
    main()