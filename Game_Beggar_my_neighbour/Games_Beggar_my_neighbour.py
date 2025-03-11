# Beggar My Neighbour
## I coded this in December 2023 during my first weeks of learning Python.
### Just added a stopping condition (if the game takes too long) just before uploading it to GitHub.

import random

# Define card colors and figures
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace',  'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10',   'Power': 10},
    {'Figure': '9',    'Power': 9}
]

# Generate all cards
all_cards = []
for color in colors:
    for figure in figures:
        card = figure.copy()
        card['Color'] = color
        all_cards.append(card)

# Shuffle cards
random.shuffle(all_cards)
print(all_cards, '\n')

# Deal cards to players
player1 = all_cards[::2]
player2 = all_cards[1::2]

print(f"Player 1 has {len(player1)} cards: {player1}\n")
print(f"Player 2 has {len(player2)} cards: {player2}\n")

# Initialize game variables
stack = []
iteration = 0
max_iterations = 10000

while player1 and player2 and iteration < max_iterations:
    # Draw cards from each player
    stack.append(player1.pop(0))
    stack.append(player2.pop(0))

    print(f"Iteration {iteration}: Card 1: {stack[0]['Figure']} {stack[0]['Color']} vs Card 2: {stack[1]['Figure']} {stack[1]['Color']}")

    if stack[0]['Power'] > stack[1]['Power']:
        player1.extend(stack)
        print(f"Player 1 wins this round. Result: {len(player1)} vs {len(player2)}\n")
    elif stack[0]['Power'] < stack[1]['Power']:
        player2.extend(stack)
        print(f"Player 2 wins this round. Result: {len(player1)} vs {len(player2)}\n")
    else:
        print("\nBattle!\n")
        battle_iteration = 1

        while stack[-2]['Power'] == stack[-1]['Power']:
            print(f"Battle iteration {battle_iteration}")

            if len(player1) < 2:
                player2.extend(stack)
                player2.extend(player1)
                print("Player 1 does not have enough cards.")
                player1 = []
                stack = []
                break
            elif len(player2) < 2:
                player1.extend(stack)
                player1.extend(player2)
                print("Player 2 does not have enough cards.")
                player2 = []
                stack = []
                break
            else:
                stack.append(player1.pop(0))  # Burn card
                stack.append(player2.pop(0))  # Burn card
                print(f"Burned cards: Card 1: {stack[-2]['Figure']} {stack[-2]['Color']} & Card 2: {stack[-1]['Figure']} {stack[-1]['Color']}")
                stack.append(player1.pop(0))  # Play card
                stack.append(player2.pop(0))  # Play card
                print(f"Battle between: Card 1: {stack[-2]['Figure']} {stack[-2]['Color']} vs Card 2: {stack[-1]['Figure']} {stack[-1]['Color']}")

                if stack[-2]['Power'] > stack[-1]['Power']:
                    player1.extend(stack)
                elif stack[-2]['Power'] < stack[-1]['Power']:
                    player2.extend(stack)
                else:
                    battle_iteration += 1
                    continue
            stack = []  # Clear the stack
            print(f"\nResult: {len(player1)} vs {len(player2)}\n")
            break

    stack = []  # Clear the stack
    iteration += 1

if iteration == max_iterations:
    print("It's a draw! Play again ;)")
else:
    if not player1:
        print("Player 2 WINS!\n")
    else:
        print("Player 1 WINS!\n")
