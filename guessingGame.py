from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

turns = 0

# function to check user guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("too low")
        return turns - 1
    else:
        print(f"you got it! the answer was {actual_answer}")



# function to set difficulty
def set_difficulty():
    level = input("chose a difficulty, type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
def game(): 
    # chosing a random number between 1 and 100.
    print("Welcome to the number guessing game!")
    print("i'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
        
    turns = set_difficulty()

    # repeating the guessing functionality if thay get it wrong
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        # let the user guess a number
        guess = int(input("make a guess: "))

        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("you run out of guesses, you lose!")
            return
        elif guess != answer:
            print("guess wrong, guess again")


    # track the number of turns and reduce by 1 if they get it wrong

game()

    