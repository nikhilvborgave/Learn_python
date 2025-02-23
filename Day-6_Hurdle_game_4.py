#this is a game: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#this solution is for hurdle-4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    
    if wall_on_right() and wall_in_front():
        turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()
