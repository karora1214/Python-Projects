# Rock, Paper, Scissors

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random as ran
user_choice = int(input("What is your choice, pick 0 for rock, 1 for paper and 2 for scissor :\n"))
comp_choice = ran.randint(0, 2)

if comp_choice == 0 and user_choice == 0:
    print("comp_choice = " + rock)
    print("user_choice = " + rock)
    print("Its a draw!")
elif comp_choice == 1 and user_choice == 0:
    print("comp_choice = " + paper)
    print("user_choice = " + rock)
    print("Computer Wins!")
elif comp_choice == 2 and user_choice == 0:
    print("comp_choice = " + scissors)
    print("user_choice = " + rock)
    print("You Wins!")
elif comp_choice == 0 and user_choice == 1:
    print("comp_choice = " + rock)
    print("user_choice = " + paper)
    print("You Wins!")
elif comp_choice == 0 and user_choice == 2:
    print("comp_choice = " + rock)
    print("user_choice = " + scissors)
    print("Computer Wins!")
elif comp_choice == 1 and user_choice == 1:
    print("comp_choice = " + paper)
    print("user_choice = " + paper)
    print("Its a draw!")
elif comp_choice == 2 and user_choice == 2:
    print("comp_choice = " + scissors)
    print("user_choice = " + scissors)
    print("Its a draw!")
else:
    print("Wrong Input, You Lose by default!")