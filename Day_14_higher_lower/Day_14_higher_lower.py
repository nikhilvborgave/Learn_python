import random
import art
import game_data

def game():
    global a_followers, b_followers, correct_ans
    if correct_ans != {}:
        choice_1 = correct_ans
        choice_2  = random.choice(game_data.data)
    else:
        choice_1 = random.choice(game_data.data)
        choice_2 = random.choice(game_data.data)
    a_followers = choice_1['follower_count']
    print(f"Compare A: {choice_1['name']}, {choice_1['description']}, from {choice_1['country']}")
    # print(a_followers)
    b_followers = choice_2['follower_count']
    while a_followers == b_followers:
        choice_2 = random.choice(game_data.data)
    print(art.vs)
    print(f"Compare B: {choice_2['name']}, {choice_2['description']}, from {choice_2['country']}")
    # print(b_followers)
    return a_followers, b_followers, choice_1, choice_2

print(art.logo)
correct_ans = {}
score = 0
continue_game = True
while continue_game:
    a_followers, b_followers, choice_1, choice_2 = game()
    guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    if a_followers > b_followers and guess == "A":
        score += 1
        correct_ans = choice_1
        print(f"Correct. Score: {score}")
    elif a_followers < b_followers and guess == "B":
        score += 1
        correct_ans = choice_2
        print(f"Correct. Score: {score}")
    elif a_followers > b_followers and guess == "B":
        continue_game = False
        print(f"Wrong. You lose. Your total score is {score}")
    elif a_followers < b_followers and guess == "A":
        continue_game = False
        print(f"Wrong. You lose. Your total score is {score}")