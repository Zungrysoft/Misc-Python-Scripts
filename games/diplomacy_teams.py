import random

def main():
    players = input("Please enter a list of player names separated by spaces:\n").split(' ')

    num_powers = 7
    player_count = len(players)
    powers = [[] for _ in range(num_powers)]
    for i in range(player_count):
        # Choose a random player
        r = int(random.random() * len(players))
        name = players[r]
        del players[r]

        # Put them on a team
        powers[i % num_powers].append(name)

    # Print title
    print()
    print("------------")
    print("Delegations:")
    print("------------")

    # Shuffle teams and print out who represents what country
    power_names = ['England', 'France', 'Germany', 'Italy', 'Austria', 'Russia', 'Turkey']
    random.shuffle(powers)
    for i in range(num_powers):
        print(f"{power_names[i]} will be represented by ", end="")
        representatives = powers[i]
        if len(representatives) == 0:
            pass
        elif len(representatives) == 1:
            print(representatives[0])
        elif len(representatives) == 2:
            print(f"{representatives[0]} and {representatives[1]}")
        else:
            for j in range(len(representatives) - 1):
                print(f"{representatives[j]}, ", end="")
            print(f"and {representatives[-1]}")

main()
