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
rock_paper_scissors = [rock, paper, scissors]
player_answer = int(input("1 for rock, 2 for paper, or 3 for scissors: ")) - 1
computer_num = random.randint(0, len(rock_paper_scissors)-1)
print(f"Enemy choice:\n{rock_paper_scissors[computer_num]}")
if player_answer == computer_num:
    print(f"Your choice:\n{rock_paper_scissors[player_answer]}")
    print("Draw!")
elif player_answer == 0 and computer_num == 2 or player_answer == 1 and computer_num == 0 or player_answer == 2 and computer_num == 1:
    print(f"Your choice:\n{rock_paper_scissors[player_answer]}")
    print("You win!")
else:
    print(f"Your choice:\n{rock_paper_scissors[player_answer]}")
    print("You lose!")
print("Press enter to exit")