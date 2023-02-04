
# since we want to randomly select an
# option from the data, we need random
# module
import random
import os
# import the game data
from data import data
from data import data_sources
 
# import the ASCII art to display.
from art import logo
import time
import datetime




def assign():
    return random.choice(data)
 

 
def play_higher_lower():
     
    # infinite loop to make user play
    # game again and again.
    playing_game = True
    while playing_game:
         
        # variable to keep track fo suer's score,
        # i.e., how many times he answers correctly
        score = 0
         
        # infinite loop to continue the current game play
        still_guessing = True
        while still_guessing:
             
            # print the logo after clearing the screen.
            os.system('clear')
            print(logo)
             
            # assign two account names to display
            person1 = assign()
             

             
            # display account1 name and description
            print(f"Title: {person1['name']}, Image: {person1['link']}")
             
            # display current score
            print("------------------------------------")
            print(f"Your current score is: {score}")
            print("------------------------------------")
             
            # ask for user input
            guess = input("""
            Is this image AI? 
            Enter '1' for YES   or   '0' for NO: """)

            # see if user is correct
            if guess == person1['ai']:
                score += 1
                print('Correct!') 
            else:
                # if user is wrong, the current game play loop stops
                print('Incorrect.')
                still_guessing = False

            if score >= 30:
                still_guessing = False
                print('Congrats! You won the game! The secret password for all the art sources is: secoetde')
                 
        # since the user was wrong in previous iteration and
        # the game ended, ask him if he want to play again.
        if score <= 5:
            print('Wow, you SUCK at this!')
        elif score <= 10:
            print('Getting better...')
        elif score <= 20:
            print('Youre pretty good.')
                 
        play_again = input("Want to Play Again? (yes/no): ").lower()
         
        # if he want to, continue, otherwise end the outer
        # loop as well. also check if the user entered some
        # other input than what is allowed
        if play_again == 'yes':
            continue
        elif play_again == 'no':
            playing_game = False
            print("Game Exited Successfully")
        else:
            playing_game = False
            print("Invalid Input Taken as no.")
 
want_to_play = input("Enter a secret code or If you want to play, yes/no!").lower()
if want_to_play == 'secoetde':
    print('Hello winner!')
    for item in data_sources:
        print(item)
elif want_to_play == 'yes':
    play_higher_lower()
elif want_to_play == 'no':
    print("Program Exit Successful.")
else:
    print("Invalid Input, Program Exited.")