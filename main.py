from art import logo
import os, sys
import random


# Star a game
def guess_number():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  num_ans = random.randint(1, 100)
  player_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  while (player_choice != 'hard' and player_choice != 'easy'):
    print("Choose again!! Choose the challenge level you want!!")
  if (player_choice == 'hard'):
    chance = 5
  elif (player_choice == 'easy'):
    chance = 10
  is_guessed = False
  while (chance):
    print(f"You have {chance} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if (guess == num_ans):
      print("Great guess. You win")
      is_guessed = True
      break
    elif (guess < num_ans):
      print("Too low.")
      chance -= 1
    elif (guess > num_ans):
      print("Too high.")
      chance -=1
  if (is_guessed == False):
    print("You've run out of guesses, you lose.")

run = True
while (run == True):
  guess_number()
  choice = input("\n You want play a new game ? Let's try again boy :)). Type 'y' to continue or 'n' to exit: ")
  if (choice == 'n'):
    run = False
  else:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
