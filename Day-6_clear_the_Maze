# this is a learning game. 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# There are few exceptions that will run in infinite loop but will be resolved at intermediate level.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
    
    else:
        turn_left()
