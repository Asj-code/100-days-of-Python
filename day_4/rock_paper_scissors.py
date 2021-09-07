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

options = [rock, paper, scissors]

selection = int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))
print("You have selected: " + options[selection])

computer_selection = random.randint(0, 2)
print("The computer has selected: " + options[computer_selection])

if selection == 0 and computer_selection == 0:
  print("It's a draw!")
elif selection == 0 and computer_selection == 1:
  print("You lose!")
elif selection == 0 and computer_selection == 2:
  print("You win")
elif selection == 1 and computer_selection == 0:
  print("You win")
elif selection == 1 and computer_selection == 1:
  print("It's a draw!")
elif selection == 1 and computer_selection == 2:
  print("You lose")
elif selection == 2 and computer_selection == 0:
  print("You lose")
elif selection == 2 and computer_selection == 1:
  print("You win")
else:
  print("It's a draw!")

# Rock, Paper, Scissor game
