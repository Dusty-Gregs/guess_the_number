from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    """Checks answer against guest. Returns number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    correct_answer = False
    while not correct_answer:
        if level.lower() == 'easy':
            correct_answer = True
            return EASY_LEVEL
        elif level.lower() == 'hard':
            correct_answer = True
            return HARD_LEVEL
        else:
            level = input("That is not a valid choice. Please type 'easy' or 'hard': ")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    answer = randint(1,100)
    print("I'm thinking of a number between 1 and 100.")

    turns = difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again.")

game()