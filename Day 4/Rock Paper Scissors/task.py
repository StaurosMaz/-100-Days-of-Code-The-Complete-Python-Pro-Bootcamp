import random
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
listRPS = [rock, paper, scissors]
comp_choice = listRPS[random.randint(0, 2)]
player_choice = listRPS[int(input("give a number between 0 and 2:\n"))]
print("comp chose:"+comp_choice+"\nplayer chose:"+player_choice)
if player_choice == 0 and comp_choice==2:
    print("you win")
elif player_choice == 1 and comp_choice==0:
    print("you win")
elif player_choice == 2 and comp_choice==1:
    print("you win")
elif player_choice == comp_choice:
    print("Draw")
else:
    print("you lose")


