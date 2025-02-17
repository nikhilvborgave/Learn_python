rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#paper beats rock 1 wins against 0
#scissors beat paper 2 wins against 1
#rock beat scissors 0 wins against 2
import random

computer_hand = random.randint(0,2)

player_hand = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

game_images = [rock, paper, scissors]

print(f"you chose: ")
print(game_images[player_hand])
print(f"computer chose: ")
print(game_images[computer_hand])

if player_hand >= 3 or player_hand < 0:
    print("You typed invalid number. You Lose.")
elif player_hand == 0 and computer_hand == 2:
    print("You win")
elif computer_hand == 0 and player_hand == 2:
    print("You lose.")
elif computer_hand == player_hand:
    print("It's a draw")
elif computer_hand > player_hand:
    print("You lose.")
elif player_hand > computer_hand:
    print("You win")
