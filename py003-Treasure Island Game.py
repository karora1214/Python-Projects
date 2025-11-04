# Treasure Island Game

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to the treasure island game")
choice1 = input("You have 2 routes ahead of you, right and left. What path do you chose : ").lower()
if choice1 == "right":
    print("You fell off a cliff. Game Over!")
elif choice1 == "left":
    choice2 = input("You have arrived at a river, would wait for a boat (type wait) or choose to swim (type swim) : ").lower()
    if choice2 == "swim":
        print("You were ripped apart by the crocodiles in the river. Game Over!!!")
    elif choice2 == "wait":
        choice3 = input("You have arrived at an cabin with 3 door (red, yellow and blue). Which do you open? : ").lower()
        if choice3 == "red":
            print("You opened the gate holding guardians of treasure and got yourself killed. Game Over!!!")
        elif choice3 == "blue":
            print("You opened the door holding wild animals who ripped you apart. Game Over!!!")
        elif choice3 == "yellow":
            print("Congratulations, you have found the treasure. You Win!!!")
        else:
            print("Wrong Choice. You Lose!!!")
    else:
        print("Wrong Choice. You Lose!!!")
else:
    print("Wrong Choice. You Lose!!!")