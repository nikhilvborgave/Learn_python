import random
import Day-11_Blackjack_art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def output(users_hand,users_current_score, computers_hand):
    print(f"Your cards : {users_hand}, Current score : {users_current_score}")
    print(f"Computer's first card {computers_hand[0]}")
    return input("Do you want next card? Type 'y' for yes and 'n' for no: ").lower()

computers_hand = random.sample(cards, 2)
users_hand = random.sample(cards, 2)

computers_current_score =  sum(computers_hand)
users_current_score = sum(users_hand)
repeat = True
while repeat:
    print(Day-11_Blackjack_art.logo)
    users_next_card = output(users_hand=users_hand, users_current_score=users_current_score, computers_hand=computers_hand)
    if users_next_card == "y":
        next_hand = random.choice(cards)
        users_hand.append(next_hand)
        users_current_score += next_hand
        print(f"Your cards: {users_hand}, Current score: {users_current_score}")
        print(f"Computer's first card: {computers_hand[0]}")
    elif users_next_card == "n":
        repeat = False
        if computers_current_score < 16:
            total = True
            while computers_current_score < 16:
                next_hand = random.choice(cards)
                computers_hand.append(next_hand)
                print(f"Computer's hand : {computers_hand}")
                computers_current_score += next_hand

                if computers_current_score >= 16:
                    total = False
        print(f"Computer's Total : {computers_current_score}")
        print(f"User's Total: {users_current_score}")

    if computers_current_score == 21:
        print("BLACKJACK!! Computer wins")
    elif users_current_score == 21:
        print("BLACKJACK! User Wins.")
    elif users_current_score == computers_current_score == 21:
        print("BLACKJACK!! Computer wins")
    elif users_current_score > 21:
        print("Computer wins")
    elif users_current_score > computers_current_score:
        print("User Wins.")
    elif users_current_score < computers_current_score:
        print("Computer Wins.")