
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

user = int(input('enter a number 1 for rock ,2 for scissors and 3 for paper: '))
if user ==1:
  print(rock)
elif user ==2:
  print(scissors)
elif user==3:
  print(paper)
else:
  print('invalid input')
computer = random.randint(1,3)
if computer ==1:
  print(rock)
elif computer ==2:
  print(scissors)
elif computer==3:
  print(paper)
else:
  print('invalid input')
if user ==1 and computer ==1:
  print('draw')
elif user == 1 and computer == 2:
  print('Player1 wins')
elif user == 1 and computer ==3:
  print('Computer wins')
elif user ==2 and computer == 1:
  print('Computer wins')
elif user == 2 and computer == 2:
  print('draw')
elif user == 2 and computer == 3:
  print('Player1 wins')
elif user == 3 and computer ==1:
  print('Player1 wins ')
elif user == 3 and computer== 2:
  print("Computer wins ")
elif user==3 and computer ==3:
  print('draw')
else:
  print('invalid input')

