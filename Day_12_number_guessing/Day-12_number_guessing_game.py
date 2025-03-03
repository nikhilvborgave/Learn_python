import random
LIVES = ""

def lives():
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    global LIVES
    if difficulty == "easy":
        LIVES = 10
    elif difficulty == "hard":
        LIVES = 5
    print(f"You have {LIVES} attempts remaining to guess the number.")

def game():
    global LIVES
    while LIVES != 0:
        guess = int(input("Make a guess: "))

        if chosen_number > guess:
            print("Too low")
            LIVES -= 1
        elif chosen_number < guess:
            print("Too high")
            LIVES -= 1
        elif chosen_number == guess:
            print("Correct. You Won!!")
            break
    if LIVES == 0:
        print(f"You lose. Correct number was {chosen_number}")


chosen_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
lives()
game()