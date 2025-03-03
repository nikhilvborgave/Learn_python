import random
numbers = []
for i in range(1, 101):
    numbers.append(i)

chosen_number = random.choice(numbers)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
Lives = ""
if difficulty == "easy":
    Lives = 10
elif difficulty == "hard":
    Lives = 5

print(f"You have {Lives} attempts remaining to guess the number.")

while Lives != 0:
    guess = int(input("Make a guess: "))

    if chosen_number > guess:
        print("Too low")
        Lives -= 1
    elif chosen_number < guess:
        print("Too high")
        Lives -= 1
    elif chosen_number == guess:
        print("Correct. You Won!!")
        break
if Lives == 0:
    print(f"You lose. Correct number was {chosen_number}")