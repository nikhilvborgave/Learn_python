print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at crossroads. Where do you want to go?")
direction = input('Type "left" or "right". ')

if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    boat = input('Type "swim" to swim across lake or "wait" to wait for a boat ')
    if boat == "wait":
        print("You arrive at island unharmed. There are 3 doors. 1. Red, 2. Blue 3. Yellow")
        door = input('Which one do you choose? Type "red" ,"blue", or "yellow" ')
        if door == "yellow":
            print("Wooooohoooo You win!!!!!!!")

        elif door == "red":
            print("Burned by fire. GAME OVER..")
        elif door == "blue":
            print("Burned by fire. GAME OVER..")
        else:
            print("Wrong input. GAME OVER..")
    else:
        print("Attacked by Crocodile. GAME OVER..")

else:
    print("Attacked by gorilla. GAME OVER..")
